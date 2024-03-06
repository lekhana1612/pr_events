from django.contrib import admin

# Register your models here.
from feedback.models import feedback

# Register your models here.
class feedbackAdmin(admin.ModelAdmin):
    list_display=('custname','email','phone','message')

admin.site.register(feedback,feedbackAdmin) 