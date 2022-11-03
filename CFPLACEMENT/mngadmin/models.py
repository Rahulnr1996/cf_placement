from django.db import models

# Create your models here.
class mregister(models.Model):
    name=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    def __str__(self):
        return self.name
    


class mdetails(models.Model):
    clgname=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    def __str__(self):
        return self.clgname

class mcompanyT(models.Model):
    cname=models.CharField(max_length=60)
    clocation=models.CharField(max_length=60)
    cvacancy=models.CharField(max_length=60)
    nvacancy=models.IntegerField()
    cdate=models.DateTimeField()
def __str___(self):
    return self.cname
