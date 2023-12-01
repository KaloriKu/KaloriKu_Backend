import datetime
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Role(models.TextChoices):
    REGISTERED_USER = 'Registered_user'
    ADMIN = "Admin"

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField()
    role = models.CharField(choices=Role.choices, default=Role.REGISTERED_USER)

    def __str__(self):
        return f"{self.user.email}/{self.nama} - {self.role}"