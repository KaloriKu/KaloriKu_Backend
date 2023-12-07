import datetime
from authentication.dataclasses.user_registration import UserRegistration
from django.contrib.auth.models import User
from authentication.models import RegisteredUser, Role
from .serializers import UserRegistrationSerializer, RegisteredUserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError, transaction
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework_simplejwt.token_blacklist.models import \
OutstandingToken, BlacklistedToken
from datetime import datetime
from pytz import timezone

# Create your views here.
class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        try:
            serializer.is_valid(raise_exception=True)
            data = UserRegistration(**serializer.validated_data)

            with transaction.atomic():
                user = User.objects.create_user(username = data.email,
                                        email = data.email,
                                        password = data.password)
                
                registered_user = RegisteredUser.objects.create(
                                                        user = user,
                                                        nama = data.nama,
                                                        umur = data.umur,
                                                        gender = data.gender,
                                                        berat_badan = data.berat_badan,
                                                        tinggi_badan = data.tinggi_badan,
                                                        tingkat_aktivitas = data.tingkat_aktivitas
                                                        )
                
                if data.role == 'Admin':
                    registered_user.role = Role.ADMIN
                    registered_user.save()
                
                response = RegisteredUserSerializer(registered_user)
                return Response(response.data, status = status.HTTP_201_CREATED)
        
        except IntegrityError:
            return Response("Credentials has been registered!", status = status.HTTP_409_CONFLICT)
        

class RefreshAPI(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        tz = timezone('Asia/Jakarta')
        BlacklistedToken.objects.filter(token__expires_at__lt=datetime.now(tz=tz)).delete()
        OutstandingToken.objects.filter(expires_at__lt=datetime.now(tz=tz)).delete()
        response = super().post(request, *args, **kwargs)
        return response