from django.db import IntegrityError,transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from authentication.models import RegisteredUser, Role
from authentication.serializers import RegisteredUserSerializer, UserRegistrationSerializer
from commons.custom_permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        registered_user = RegisteredUser.objects.get(user = request.user)
        serializer = RegisteredUserSerializer(registered_user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def patch(self, request):
        registered_user = RegisteredUser.objects.get(user = request.user)
        serializer = UserRegistrationSerializer(data = request.data, partial = True)
        try:
            if (serializer.is_valid()):
                with transaction.atomic():
                    user = request.user

                    if (serializer.validated_data.get('password') != None):
                        user.set_password(serializer.validated_data.get('password'))

                    if (serializer.validated_data.get('email') != None):
                        user.username = serializer.validated_data.get('email', registered_user.user.get_username())
                        user.email = serializer.validated_data.get('email', registered_user.user.get_username())
                    
                    registered_user.user = user
                    registered_user.nama = serializer.validated_data.get('nama', registered_user.nama)
                    
                    user.save()
                    registered_user.save()

                    serializer = RegisteredUserSerializer(registered_user)
                    return Response(serializer.data, status = status.HTTP_200_OK)
                
        except IntegrityError as e:
            return Response(e)
        
class AllRegisteredUserProfileAPI(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        registered_user = RegisteredUser.objects.filter(role = Role.REGISTERED_USER)
        serializer = RegisteredUserSerializer(registered_user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
        
        