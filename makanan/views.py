import json
from django import http
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from makanan.models import Makanan

# Create your views here.
class GetDaftarMakananAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Data makanan di-scrape dari website: https://andrafarm.com//_andra.php?_i=daftar-tkpi&jobs=&perhal=2000&urut=1&asc=0000000000&sby=&no1=2&knama=&ref=adityawarmanfw.id
        yang bersumber dari Data Tabel Komposisi Pangan Indonesia (TKPI) 2019
        """
        try:
            userId = request.user.id
            allMakanan = Makanan.objects.filter(userId=0).order_by('nama')
            allMakananSaya = Makanan.objects.filter(userId=userId).order_by('nama')
            daftarMakanan = {
                'allMakanan': list(allMakanan.values()),
                'allMakananSaya': list(allMakananSaya.values())
            }
            return Response(daftarMakanan, content_type='application/json', status=status.HTTP_200_OK)
        except:
            return Response("Makanan tidak berhasil ditampilkan", status=status.HTTP_400_BAD_REQUEST)

def isMakananValid(userId, nama):
    allMakananDenganNama = Makanan.objects.filter(userId=0, nama=nama).values()
    allMakananSayaDenganNama = Makanan.objects.filter(userId=userId, nama=nama).values()
    if len(allMakananDenganNama | allMakananSayaDenganNama) > 0:
        return False
    else:
        return True

class AddMakananSayaAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not isMakananValid(request.user.id, request.POST.get('nama')):
            return Response("Makanan sudah terdaftar", status=status.HTTP_400_BAD_REQUEST)

        try:
            makanan = Makanan.objects.create(
                userId=request.user.id,
                nama=request.POST.get('nama'),
                jumlahKalori=request.POST.get('jumlahKalori'),
                jumlahLemak=request.POST.get('jumlahLemak'),
                jumlahKarbohidrat=request.POST.get('jumlahKarbohidrat'),
                jumlahProtein=request.POST.get('jumlahProtein')
            )
            makanan.save()
            return Response("Makanan berhasil disimpan", status=status.HTTP_200_OK)
        except:
            return Response("Makanan tidak berhasil disimpan", status=status.HTTP_400_BAD_REQUEST)