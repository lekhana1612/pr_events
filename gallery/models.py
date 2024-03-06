from django.db import models

# Create your models here.

class Decoration(models.Model):
    customer_id=models.CharField(null=True,max_length=10)
    option = models.CharField(max_length=20)
    customization=models.CharField(max_length=100)