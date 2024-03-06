from django import forms


from customerdata.models import customerdata

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customerdata
        fields=['customername','email','phone','eventname','eventdate','eventcity','eventvenue','pincode','quotation','advance','balance','description']
        exclude=['customer_id']