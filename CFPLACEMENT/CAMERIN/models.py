from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=60)
    def __str__(self):
        return self.name