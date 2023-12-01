from django.urls import path
from makanan.views import GetDaftarMakananAPI, AddMakananSayaAPI

app_name = 'makanan'

urlpatterns = [
    path('all', GetDaftarMakananAPI.as_view(), name='get_daftar_makanan'),
    path('add', AddMakananSayaAPI.as_view(), name='add_makanan_saya'),
]