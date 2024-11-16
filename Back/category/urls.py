from django.urls import  path
from .views import CategoryListCreate, CategoryDetail

urlpatterns = [
    path('', CategoryListCreate.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]