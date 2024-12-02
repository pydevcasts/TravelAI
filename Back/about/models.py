from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    Establishment = models.PositiveIntegerField()# تاسیس 
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title