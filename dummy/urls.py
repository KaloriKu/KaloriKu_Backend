from django.urls import path, include
from dummy.views import AllDummiesAPI, DummyAPI, ProtectedDummyAPI, AdminDummyAPI

app_name = 'dummy'

urlpatterns = [
    path('', DummyAPI.as_view(), name = 'dummy'),
    path('all', AllDummiesAPI.as_view(), name = 'all'),
    path('protected', ProtectedDummyAPI.as_view(), name = 'protected'),
    path('admin', AdminDummyAPI.as_view(), name = 'admin'),
]