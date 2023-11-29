from django.urls import path
from makanan.views import getDaftarMakanan, addMakananSaya

app_name = 'makanan'

urlpatterns = [
    path('all/<int:userId>', getDaftarMakanan, name='getDaftarMakanan'),
    path('add/', addMakananSaya, name='addMakananSaya'),
]