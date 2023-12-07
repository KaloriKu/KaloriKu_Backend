from django.urls import path
from authentication.views import UserRegistrationAPIView, RefreshAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


app_name = 'authentication'

urlpatterns = [
    path('register', UserRegistrationAPIView.as_view(), name = 'register'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', RefreshAPI.as_view(), name='token_refresh'),
]