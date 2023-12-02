from rest_framework import serializers
from authentication.models import RegisteredUser
from django.contrib.auth.models import User
from .models import Role
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    nama = serializers.CharField()
    role = serializers.ChoiceField(choices=Role.choices, default = Role.REGISTERED_USER)
    berat_badan = serializers.FloatField(default = None)
    tinggi_badan = serializers.FloatField(default = None)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        exclude =('password','is_superuser','last_login',
            'is_staff','is_active','date_joined','groups',
            'user_permissions','first_name','last_name',)

class RegisteredUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model =  RegisteredUser
        fields = '__all__' 

class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
