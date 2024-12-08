from django.urls import include, path
from rest_framework import routers

from .views import BlogViewSet

app_name = "blog"


router = routers.SimpleRouter()
router.register('', BlogViewSet, basename='blog')

urlpatterns = [
    path("", include(router.urls)),
]