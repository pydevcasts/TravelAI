from django.db import models

# Create your models here.


class Contactus(models.Model):
    name = models.CharField(max_length=125, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=125, null=True, blank=True)
    message = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        verbose_name = "contactus"
        verbose_name_plural = "contactsus"

    def __str__(self):
        return self.name
