from django.contrib import admin
from remainingAmt.models import AdvanceAmount

# Register your models here.
class contactAd(admin.ModelAdmin):
    list_display=('quotation','advance','balance')

admin.site.register(AdvanceAmount,contactAd)