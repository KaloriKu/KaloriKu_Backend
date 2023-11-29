import json
from django import http
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from makanan.models import Makanan

"""
Ketika deploy pertama kali jangan lupa 
python manage.py makemigrations
python manage.py migrate 
python manage.py loaddata sample
"""
# Create your views here.
def getDaftarMakanan(request, userId):
    if request.method == 'GET':
        """
        Data makanan diambil dari website: https://andrafarm.com//_andra.php?_i=daftar-tkpi&jobs=&perhal=2000&urut=1&asc=0000000000&sby=&no1=2&knama=&ref=adityawarmanfw.id
        yang bersumber dari Data Tabel Komposisi Pangan Indonesia (TKPI) 2019
        """
        try:
            allMakanan = Makanan.objects.filter(userId=0)
            allMakananSaya = Makanan.objects.filter(userId=userId)
            daftarMakanan = {
                'allMakanan': list(allMakanan.values()),
                'allMakananSaya': list(allMakananSaya.values())
            }
            return http.HttpResponse(json.dumps(daftarMakanan), content_type='application/json', status=200)
        except:
            return http.HttpResponse("Makanan tidak berhasil ditampilkan", status=400)

def isMakananValid(userId, nama):
    allMakananDenganNama = Makanan.objects.filter(userId=0, nama=nama).values()
    allMakananSayaDenganNama = Makanan.objects.filter(userId=userId, nama=nama).values()
    if len(allMakananDenganNama | allMakananSayaDenganNama) > 0:
        return False
    else:
        return True

@csrf_exempt
def addMakananSaya(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        if not isMakananValid(body['userId'], body['nama']):
            return http.HttpResponse("Makanan sudah terdaftar", status=400)

        try:
            makanan = Makanan.objects.create(
                userId=body['userId'],
                nama=body['nama'],
                jumlahKalori=body['jumlahKalori'],
                jumlahLemak=body['jumlahLemak'],
                jumlahKarbohidrat=body['jumlahKarbohidrat'],
                jumlahProtein=body['jumlahProtein']
            )
            makanan.save()
            return http.HttpResponse("Makanan berhasil disimpan", status=200)
        except:
            return http.HttpResponse("Makanan tidak berhasil disimpan", status=400)