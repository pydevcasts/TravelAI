# users/filters.py

import django_filters
from .models import CustomGroup, CustomUser


class GroupFilter(django_filters.FilterSet):
    min_participants = django_filters.NumberFilter(field_name='min_participants', lookup_expr='gte')
    max_participants = django_filters.NumberFilter(field_name='max_participants', lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = CustomGroup
        fields = ['min_participants', 'max_participants', 'name']


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username',lookup_expr='icontains')  # فیلتر بر اساس نام
    group_name = django_filters.CharFilter(field_name='group__name', lookup_expr='icontains')
    
    class Meta:
        model = CustomUser
        fields = ['username', 'group_name']  # فیلتر بر اساس گروه هم اضافه شده است
