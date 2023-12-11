import datetime
from django.shortcuts import render
from django import http
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from rest_framework.response import Response
from commons.custom_permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Create your views here.
from artikel.models import Artikel

class GetDaftarArtikelAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            data_artikel =[]
            daftarArtikel = Artikel.objects.all()
            for item in daftarArtikel:
                data_artikel.append({
                    "id" : item.pk,            
                    "judulArtikel" : item.judulArtikel,
                    "isiArtikel" : item.isiArtikel,
                    "tanggalDiunggah" : item.tanggalDiunggah,
        
                    })
            daftar_artikel = {'allArtikel':data_artikel} 
            return Response(daftar_artikel, content_type='application/json', status=status.HTTP_200_OK)
        except:
            return Response("Gagal menampilkan artikel", status=status.HTTP_400_BAD_REQUEST)

class AddArtikelAPI(APIView):
    permission_classes = [IsAdmin]
    def post(self, request):
        body = json.loads(request.body)
        try:
            judulArtikel = body['judulArtikel']
            isiArtikel = body['isiArtikel']
            tanggalDiunggah = datetime.date.today()
            new_article = Artikel( judulArtikel=judulArtikel, isiArtikel=isiArtikel,tanggalDiunggah=tanggalDiunggah)
            new_article.save()
        
            return Response("Artikel berhasil disimpan", status=status.HTTP_200_OK)
        except:
            return Response("Gagal menyimpan artikel", status=status.HTTP_400_BAD_REQUEST)

class GetArtikelByIdAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        try: 
            artikel_by_id = Artikel.objects.get(id=id)
            artikel = []
            artikel.append({
                    "id" : artikel_by_id.pk,           
                    "judulArtikel" : artikel_by_id.judulArtikel,
                    "isiArtikel" : artikel_by_id.isiArtikel,
                    "tanggalDiunggah" : artikel_by_id.tanggalDiunggah,
    
                    })
            return Response(artikel, status=status.HTTP_200_OK)
        except:
            return Response("Gagal menampilkan artikel",status=status.HTTP_400_BAD_REQUEST)

