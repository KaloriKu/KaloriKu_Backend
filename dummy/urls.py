from django.urls import path, include
from dummy.views import dummy, allDummies, createDummy

app_name = 'dummy'

urlpatterns = [
    path('', dummy, name = 'dummy'),
    path('all/', allDummies, name = 'all'),
    path('create/', createDummy, name = 'create'),
]