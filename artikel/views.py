import datetime
from django.shortcuts import render
from django import http
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from commons.custom_permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

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
            return JsonResponse(data_artikel, safe=False)
        except:
            return http.HttpResponse("Gagal menampilkan artikel",status=400)

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
        
            return http.HttpResponse("Artikel berhasil disimpan", status=200)
        except:
            return http.HttpResponse("Gagal menyimpan artikel", status=400)

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
            return JsonResponse(artikel, safe=False)
        except:
            return http.HttpResponse("Gagal menampilkan artikel",status=400)

