from django.db import models

# Create your models here.
class Artikel(models.Model):
    judulArtikel = models.CharField()
    isiArtikel = models.TextField(blank=True)
    tanggalDiunggah = models.DateTimeField(auto_now_add = True)