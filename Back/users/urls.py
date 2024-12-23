# users/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import (
    CustomUserViewSet,
    GroupViewSet,
    RatingViewSet,
    RequestViewSet,
    TripViewSet,
)


router = DefaultRouter()
router.register(r"users", CustomUserViewSet)
router.register(r"groups", GroupViewSet, basename="group")
router.register(r"trips", TripViewSet)
router.register(r"requests", RequestViewSet)
router.register(r"ratings", RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/login/', CustomLoginView.as_view(), name='custom_login'),

]
