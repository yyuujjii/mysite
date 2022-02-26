from django.db import models

# Create your models here.


class People(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tell = models.CharField(max_length=100)
    sender = models.EmailField(max_length=100)
    message = models.CharField(max_length=500)
    myself = models.BooleanField()
