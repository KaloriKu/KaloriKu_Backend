from django.shortcuts import render
from authentication.dataclasses.user_registration import UserRegistration
from django.contrib.auth.models import User
from authentication.models import RegisteredUser, Role
from .serializers import UserRegistrationSerializer, RegisteredUserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError, transaction

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
                
                registered_user = RegisteredUser.objects.create(user = user,
                                                        nama = data.nama)
                
                if data.role == 'Admin':
                    registered_user.role = Role.ADMIN
                
                response = RegisteredUserSerializer(registered_user)
                return Response(response.data, status = status.HTTP_201_CREATED)
        
        except IntegrityError:
            return Response("Credentials has been registered!", status = status.HTTP_409_CONFLICT)