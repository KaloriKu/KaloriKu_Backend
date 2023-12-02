import json
from django.shortcuts import render
from django import http
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from makanan.models import Makanan
from makanan_dikonsumsi.models import MakananDikonsumsi
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status


# Create your views here.
class GetDaftarMakananDikonsumsi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            userId = request.user.id
            allMakananDikonsumsi = MakananDikonsumsi.objects.filter(userId=userId)
                
            # Serialize the queryset into JSON
            serializedData = serializers.serialize('json', allMakananDikonsumsi)
            records = json.loads(serializedData)

            list_data = []

            for record in records:
                data = {}
                listDetailMakanan = []
                totalKalori = 0
                totalLemak = 0
                totalKarbohidrat = 0
                totalProtein = 0

                timeStamp = record['fields']['timeStamp']
                listMakanan = record['fields']['makanan']
                print(listMakanan)
    
                for idMakanan in listMakanan:
                    detailMakanan = {}
                    makananInstance = Makanan.objects.get(id=idMakanan)

                    nama = makananInstance.nama
                    jumlahKalori = makananInstance.jumlahKalori
                    jumlahLemak = makananInstance.jumlahLemak
                    jumlahKarbohidrat = makananInstance.jumlahKarbohidrat
                    jumlahProtein = makananInstance.jumlahProtein

                    totalKalori += jumlahKalori
                    totalLemak += jumlahLemak
                    totalKarbohidrat += jumlahKarbohidrat
                    totalProtein += jumlahProtein

                    detailMakanan['nama'] = nama
                    detailMakanan['jumlahKalori'] = jumlahKalori
                    detailMakanan['jumlahLemak'] = jumlahLemak
                    detailMakanan['jumlahKarbohidrat'] = jumlahKarbohidrat
                    detailMakanan['jumlahProtein'] = jumlahProtein
                    
                    listDetailMakanan.append(detailMakanan)

                data['timeStamp'] = timeStamp
                data['totalKalori'] = totalKalori
                data['totalLemak'] = totalLemak
                data['totalKarbohidrat'] = totalKarbohidrat
                data['totalProtein'] = totalProtein            
                data['details'] = listDetailMakanan

                list_data.append(data)
            

            return JsonResponse({'data': list_data}, status=200)
        except:
            return http.HttpResponse("Daftar Makanan Dikonsumsi tidak berhasil ditampilkan", status=400)
        
class AddMakananDikonsumsi(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        body = json.loads(request.body)

        try:
            makananDikonsumsi = MakananDikonsumsi.objects.create(
                userId=request.user.id
            )
            for id in body['makanan']:
                makananInstance = Makanan.objects.get(id=id)
                makananDikonsumsi.makanan.add(makananInstance)
            makananDikonsumsi.save()
            return http.HttpResponse("Daftar Makanan Dikonsumsi berhasil disimpan", status=200)
        except:
            return http.HttpResponse("Daftar Makanan Dikonsumsi tidak berhasil disimpan", status=400)