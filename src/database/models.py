from django.db import models

# Create your models here.



class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)