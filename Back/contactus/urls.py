from django.urls import include, path
from rest_framework import routers

from contactus.views import ContactusViewSet

app_name = "contactus"


router = routers.SimpleRouter()
router.register('', ContactusViewSet, basename='contactus')
urlpatterns = [
    path("", include(router.urls)),
]