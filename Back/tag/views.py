from .models import Tag
from rest_framework.viewsets import ModelViewSet
from .serializers import TagSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    search_fields = [
        'name',
    ]
