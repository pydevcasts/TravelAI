from about.views import AboutViewSet
from django.urls import include, path
from rest_framework import routers

app_name = "about"


router = routers.SimpleRouter()
router.register("", AboutViewSet, basename="about")
urlpatterns = [
    path("", include(router.urls)),
]
