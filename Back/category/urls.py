from django.urls import path

from .views import CategoryDetail, CategoryListCreate

urlpatterns = [
    path("", CategoryListCreate.as_view(), name="category-list-create"),
    path("<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
]
