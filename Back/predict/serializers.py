# api/serializers.py

from rest_framework import serializers
from .models import BostonHousing

class BostonHousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BostonHousing
        fields = ['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']