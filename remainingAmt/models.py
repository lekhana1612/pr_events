from django.db import models
from customerdata.models import customerdata
# Create your models here.
class AdvanceAmount(models.Model):
    customer_id = models.ForeignKey(customerdata, on_delete=models.CASCADE)
    quotation=models.CharField(max_length=50)
    advance = models.DecimalField(max_digits=10, decimal_places=2)
    balance=models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Advance amount of {self.advance} for {self.customerdata.customername}"
