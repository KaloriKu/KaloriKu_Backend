from django.urls import path
from makanan_dikonsumsi.views import GetDaftarMakananDikonsumsi, AddMakananDikonsumsi

app_name = 'makanan_dikonsumsi'

urlpatterns = [
    path('all', GetDaftarMakananDikonsumsi.as_view(), name='get_daftar_makanan_dikonsumsi'),
    path('add', AddMakananDikonsumsi.as_view(), name='add_makanan_dikonsumsi'),
]