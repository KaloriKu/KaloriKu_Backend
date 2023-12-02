from django.urls import path
from target.views import GetTargetAPI, EditTargetAPI

app_name = 'target'

urlpatterns = [
    path('', GetTargetAPI.as_view(), name='get_target'),
    path('edit', EditTargetAPI.as_view(), name='edit_target')
]