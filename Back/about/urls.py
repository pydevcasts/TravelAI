from django.urls import include, path
from rest_framework import routers

from about.views import AboutViewSet

app_name = "about"


router = routers.SimpleRouter()
router.register('', AboutViewSet, basename='about')
urlpatterns = [
    path("", include(router.urls)),
]