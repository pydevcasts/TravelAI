# api/models.py

from django.db import models

class BostonHousing(models.Model):
    crim = models.FloatField()
    zn = models.FloatField()
    indus = models.FloatField()
    chas = models.IntegerField()
    nox = models.FloatField()
    rm = models.FloatField()
    age = models.FloatField()
    dis = models.FloatField()
    rad = models.IntegerField()
    tax = models.FloatField()
    ptratio = models.FloatField()
    b = models.FloatField()
    lstat = models.FloatField()
    medv = models.FloatField(blank=True, null=True)  

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction: {self.medv} at {self.created_at}"