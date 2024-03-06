from django.contrib import admin
from customerdata.models import customerdata

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display=('customer_id','customername','phone','email','eventdate','eventname','eventvenue','eventcity','pincode','quotation','advance','balance','description')

admin.site.register(customerdata,contactAdmin)

# Register your models here.
