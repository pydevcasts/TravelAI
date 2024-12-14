from django.urls import include, path
from rest_framework import routers

from .views import TagViewSet

app_name = "tag"


router = routers.SimpleRouter()
router.register("", TagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
]
