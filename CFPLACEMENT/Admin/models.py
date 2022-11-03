from django.db import models
from CAMERIN . models import register

# Create your models here.
class Adlogin(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    def __str__(self):
        return self.username
