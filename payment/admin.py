from django.contrib import admin
from payment.models import payment

# Register your models here.
class paymentAdmin(admin.ModelAdmin):
    list_display=('customer_id','amount', 'card_number', 'expiration_date', 'cvv','utr')

admin.site.register(payment,paymentAdmin)