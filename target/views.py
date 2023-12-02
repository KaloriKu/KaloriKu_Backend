import requests
from django.shortcuts import render
from target.models import Target
# from user_profile.models import modelnyyyy
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GetTargetAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            userId = request.user.id
            target = Target.objects.filter(userId=userId)
            return Response(target, content_type='application/json', status=status.HTTP_200_OK)
        except:
            return Response("Gagal menampilkan target", status=status.HTTP_400_BAD_REQUEST)

def count_kalori(self, request, age, gender, height, weight):
        # URL of the external API
        api_url = f"https://fitness-calculator.p.rapidapi.com/dailycalorie?age={age}&gender={gender}&height={height}&weight={weight}&activitylevel=level_1"

        # Headers to be included in the request
        headers: {
            'X-RapidAPI-Key': '3c1c10e885msh33f21c29898edb6p1cd35fjsn4a3dc124364d',
            'X-RapidAPI-Host': 'fitness-calculator.p.rapidapi.com'
        }

        # Make a GET request to the API with headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Process the API response (assuming it returns JSON data)
            api_data = response.json()

            # Do something with the data, for example, return it as JSON
            return JsonResponse(api_data)
        else:
            # If the request was not successful, handle the error
            error_message = "Failed to fetch data from the API"
            return JsonResponse({'error': error_message}, status=response.status_code)
        
        
class EditTargetAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            targetKaloriHarian = count_kalori(self, request, )
            target = Target.objects.create(
                userId=request.user.id,
                tujuan=request.POST.get('tujuan'),
                jangkaWaktu=request.POST.get('jangkaWaktu'),
                # filter tujuan duluu
                targetKaloriHarian=targetKaloriHarian
            )
            target.save()
            return Response("Target berhasil disimpan", status=status.HTTP_200_OK)
        except:
            return Response("Target tidak berhasil disimpan", status=status.HTTP_400_BAD_REQUEST)