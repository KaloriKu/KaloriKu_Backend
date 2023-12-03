from django.db import models

# Create your models here.

class Target(models.Model):
    userId = models.IntegerField()
    tujuan = models.CharField(max_length=30)
    jangkaWaktu = models.IntegerField()
    perubahanBeratBadan = models.IntegerField(default=None, null=True, blank=True)
    targetKaloriHarian = models.FloatField()