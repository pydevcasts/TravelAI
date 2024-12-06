from django.shortcuts import render


from .models import Blog
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer




class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    search_fields = [
        'name', 
    ]
