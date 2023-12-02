from django.urls import path
from artikel.views import GetArtikelByIdAPI,GetDaftarArtikelAPI,AddArtikelAPI

app_name = 'artikel'

urlpatterns = [
    path('all', GetDaftarArtikelAPI.as_view(), name='getAllArtikel'),
    path('add',AddArtikelAPI.as_view(),name='addArtikel'),
    path('<int:id>',GetArtikelByIdAPI.as_view(), name = 'getArtikelById')
]