from django.db import models

# Create your models here.
class feedback(models.Model):
    custname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.TextField()
