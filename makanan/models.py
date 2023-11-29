from django.db import models

# Create your models here.
class Makanan(models.Model):
    userId = models.IntegerField()
    nama = models.CharField()
    jumlahKalori = models.FloatField()
    jumlahLemak = models.FloatField()
    jumlahKarbohidrat = models.FloatField()
    jumlahProtein = models.FloatField()