from rest_framework import serializers
from authentication.models import RegisteredUser
from django.contrib.auth.models import User
from .models import ActivityLevel, Gender, Role
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(default = None)
    password = serializers.CharField(default = None)
    nama = serializers.CharField(default = None)
    umur = serializers.IntegerField(default = None)
    gender = serializers.ChoiceField(choices=Gender.choices, default = None)
    berat_badan = serializers.FloatField(default = None)
    tinggi_badan = serializers.FloatField(default = None)
    role = serializers.ChoiceField(choices=Role.choices, default = Role.REGISTERED_USER)
    tingkat_aktivitas = serializers.ChoiceField(choices=ActivityLevel.choices,
                                                default = ActivityLevel.LEVEL_1)

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
