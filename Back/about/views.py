from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from about.models import About
from about.serializers import AboutSerializer


# Create your views here.
class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    search_fields = [
        'title', 'content',
    ]
    