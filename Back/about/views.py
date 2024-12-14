<<<<<<< HEAD
from rest_framework.viewsets import ModelViewSet
=======
>>>>>>> master
from about.models import About
from about.serializers import AboutSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    search_fields = [
<<<<<<< HEAD
        'title', 'description',
=======
        "title",
        "content",
>>>>>>> master
    ]
