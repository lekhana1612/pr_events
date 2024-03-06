from django import forms
from payment.models import payment
# Create your models here.

class PaymentForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = ['customer_id','amount', 'card_number', 'expiration_date', 'cvv','utr']  # Example fields, adjust as needed
        widgets = {
            'expiration_date': forms.DateInput(attrs={'placeholder': 'MM/YYYY'}),  # Example placeholder
        }