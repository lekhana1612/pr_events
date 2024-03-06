from django.contrib import admin
from gallery.models import Decoration

# Register your models here.
class decoAdmin(admin.ModelAdmin):
    list_display=('customer_id','option','customization')


admin.site.register(Decoration,decoAdmin)