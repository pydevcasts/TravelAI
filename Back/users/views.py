from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import CustomUser,  Group, Rating, Request, Trip
from .serializers import RatingSerializer, RequestSerializer, TripSerializer, UserSerializer, GroupSerializer
from .filters import GroupFilter, UserFilter
from rest_framework.permissions import IsAdminUser



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.select_related('group').all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    permission_classes = [IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['min_participants', 'max_participants', 'name']
    ordering_fields = ['name', 'min_participants', 'max_participants']
    ordering = ['name']  # Default ordering
    filterset_class = GroupFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return Group.objects.all()
        else:
            return Group.objects.filter(status=True)



class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer