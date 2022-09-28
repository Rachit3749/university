from django.db import models


# Create your models here.
class reg(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    age = models.CharField(max_length=5)
