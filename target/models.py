from django.db import models

# Create your models here.
class Target(models.Model):
    userId = models.IntegerField()
    tujuan = models.CharField(max_length=20)
    jangkaWaktu = models.IntegerField()
    targetKaloriHarian = models.FloatField()