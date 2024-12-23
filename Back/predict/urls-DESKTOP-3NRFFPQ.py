from django.urls import path

from .views import BostonHousingDetailView, BostonHousingListCreateView

urlpatterns = [
    path("", BostonHousingListCreateView.as_view(), name="bostonhousing-list-create"),
    path("<int:pk>/", BostonHousingDetailView.as_view(), name="bostonhousing-detail"),
]
