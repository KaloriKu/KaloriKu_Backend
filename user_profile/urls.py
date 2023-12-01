from django.urls import path
from user_profile.views import ProfileAPI, AllRegisteredUserProfileAPI

app_name = "user_profile"

urlpatterns = [
    path('', ProfileAPI.as_view(), name = 'profile'),
    path('all', AllRegisteredUserProfileAPI.as_view(), name = 'all')
]
