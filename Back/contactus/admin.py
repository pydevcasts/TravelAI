from django.contrib import admin

from contactus.models import Contactus

# Register your models here.
@admin.register(Contactus)
class reservationadmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']
