from django.db import models
from makanan.models import Makanan

# Create your models here.
class MakananDikonsumsi(models.Model):
    userId = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now_add = True)
    makanan = models.ManyToManyField(Makanan)