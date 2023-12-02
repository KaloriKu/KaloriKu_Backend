import datetime
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Role(models.TextChoices):
    REGISTERED_USER = 'Registered_user'
    ADMIN = "Admin"

class Gender(models.TextChoices):
    LAKI_LAKI = 'Laki-laki'
    PEREMPUAN = 'Perempuan'

class ActivityLevel(models.TextChoices):
    LEVEL_1 = 'Level_1'
    LEVEL_2 = 'Level_2'
    LEVEL_3 = 'Level_3'
    LEVEL_4 = 'Level_4'
    LEVEL_5 = 'Level_5'

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField()
    umur = models.IntegerField(default=None, null=True)
    gender = models.CharField(choices=Gender.choices, default=None, null=True)
    berat_badan = models.FloatField(default=None, null=True, blank=True)
    tinggi_badan = models.FloatField(default=None, null=True, blank=True)
    role = models.CharField(choices=Role.choices, default=Role.REGISTERED_USER)
    tingkat_aktivitas = models.CharField(choices=ActivityLevel.choices, 
                                         default=ActivityLevel.LEVEL_1)


    def __str__(self):
        return f"{self.user.email}/{self.nama} - {self.role}"