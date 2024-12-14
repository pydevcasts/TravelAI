from contactus.models import Contactus
from django.contrib import admin


# Register your models here.
@admin.register(Contactus)
class reservationadmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]
