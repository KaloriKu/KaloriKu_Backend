import json
import requests
from target.models import Target
from authentication.models import RegisteredUser
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

class GetTargetAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            userId = request.user.id
            target = Target.objects.filter(userId=userId)
            # target = json.pa
            target = serializers.serialize("json", target)
            return HttpResponse(target, content_type='application/json', status=status.HTTP_200_OK)
        except:
            return Response(f"Gagal menampilkan target", status=status.HTTP_400_BAD_REQUEST)

def count_kalori(self, request, age, gender, height, weight, activity_level):
        """
        Perhitungan kalori menggunakan external API dari:
        https://rapidapi.com/malaaddincelik/api/fitness-calculator
        """
        
        api_url = f"https://fitness-calculator.p.rapidapi.com/dailycalorie?age={age}&gender={gender}&height={height}&weight={weight}&activitylevel={activity_level}"
        headers = {
            'X-RapidAPI-Key': '3c1c10e885msh33f21c29898edb6p1cd35fjsn4a3dc124364d',
            'X-RapidAPI-Host': 'fitness-calculator.p.rapidapi.com'
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            api_data = response.json()
            return api_data
        else:
            error_message = "Failed to fetch data from the API"
            return JsonResponse({'error': error_message}, status=response.status_code)
        
        
class EditTargetAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = RegisteredUser.objects.get(user = request.user)
            age = user.umur
            if user.gender == 'Perempuan':
                gender = 'female'
            else: 
                gender = 'male'
            height = int(user.tinggi_badan)
            weight = int(user.berat_badan)
            activity_level = user.tingkat_aktivitas.lower()
            kalori = count_kalori(self, request, age, gender, height, weight, activity_level)
            if type(kalori) != dict :
                return Response(f"Perhitungan kalori gagal", status=status.HTTP_400_BAD_REQUEST)
                
            tujuan = request.POST.get('tujuan')
            jangkaWaktu = request.POST.get("jangkaWaktu")
            perubahanBeratBadan = request.POST.get('perubahanBeratBadan')
            perubahanPerMinggu = int(perubahanBeratBadan) / int(jangkaWaktu)
            
            if tujuan == "Menjaga berat badan":
                perubahanBeratBadan = 0
                targetKaloriHarian = kalori['data']['goals']['maintain weight']
            
            elif tujuan == "Menaikkan berat badan":
                if perubahanPerMinggu < 0.5:
                    targetKaloriHarian = kalori['data']['goals']['Mild weight gain']['calory']
                elif perubahanPerMinggu == 0.5:
                    targetKaloriHarian = kalori['data']['goals']['Weight gain']['calory']
                else:
                    targetKaloriHarian = kalori['data']['goals']['Extreme weight gain']['calory']     
            
            elif tujuan == "Menurunkan berat badan":
                if perubahanPerMinggu < 0.5:
                    targetKaloriHarian = kalori['data']['goals']['Mild weight loss']['calory']
                elif perubahanPerMinggu == 0.5:
                    targetKaloriHarian = kalori['data']['goals']['Weight loss']['calory']
                else:
                    targetKaloriHarian = kalori['data']['goals']['Extreme weight loss']['calory']  
            
            else:
                return Response(f"Masukkan tujuan yang valid!", status=status.HTTP_400_BAD_REQUEST)
            
            try:
                # update
                target = Target.objects.get(userId = request.user.id)
                target.tujuan = tujuan
                target.jangkaWaktu = request.POST.get("jangkaWaktu")
                target.perubahanBeratBadan = perubahanBeratBadan
                target.targetKaloriHarian = targetKaloriHarian
                target.save()
                
            except:
                # create
                new_target = Target.objects.create(
                    userId=request.user.id,
                    tujuan=tujuan,
                    jangkaWaktu=request.POST.get("jangkaWaktu"),
                    perubahanBeratBadan=perubahanBeratBadan,
                    targetKaloriHarian=targetKaloriHarian
                )
                new_target.save()
            return Response("Target berhasil disimpan", status=status.HTTP_200_OK)
        except:
            return Response(f"Target tidak berhasil disimpan", status=status.HTTP_400_BAD_REQUEST)