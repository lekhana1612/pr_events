from django.db import models


# Create your models here.
class customerdata(models.Model):
    
    customer_id = models.CharField(unique=True,primary_key=True,max_length=4)
    customername=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    eventdate=models.DateField(max_length=50)
    eventname=models.CharField(max_length=50)
    eventvenue=models.CharField(max_length=50)
    eventcity=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    quotation=models.CharField(max_length=50)
    advance=models.CharField(max_length=50)
    balance=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
  
