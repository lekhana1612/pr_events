from django.db import models

class payment(models.Model):
    customer_id=models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=16)
    expiration_date = models.IntegerField()
    cvv = models.CharField(max_length=4)
    utr = models.CharField(max_length=18)
    

    def __str__(self):
        return f"${self.amount} - {self.card_number[-4:]}"
    
    