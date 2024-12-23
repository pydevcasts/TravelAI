from django_filters.rest_framework import DjangoFilterBackend

from .models import CustomUser, CustomGroup, Rating, Request, Trip
from rest_framework import filters, status, viewsets

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .standardresponse import StandardResponseMixin
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView

from .filters import GroupFilter, UserFilter
from .serializers import (
    GroupSerializer,
    RatingSerializer,
    RequestSerializer,
    TripSerializer,
    UserSerializer,
)



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.select_related("group").all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = CustomUser.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return self.success_response(data=serializer.data, user=request.user, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return self.success_response(data=serializer.data, user=request.user, status=status.HTTP_201_CREATED)
        return self.error_response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):  # For PUT
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return self.success_response(data=serializer.data, user=request.user, status=status.HTTP_200_OK)
        return self.error_response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):  # For PATCH
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):  # For DELETE
        instance = self.get_object()
        self.perform_destroy(instance)
        return self.success_response(
            data={"message": f"User with ID {instance.id} has been deleted."},
            user=request.user,
            status=status.HTTP_204_NO_CONTENT
        )


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ["min_participants", "max_participants", "name"]
    ordering_fields = ["name", "min_participants", "max_participants"]
    ordering = ["name"]  # Default ordering
    filterset_class = GroupFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return CustomGroup.objects.all()
        else:
            return CustomGroup.objects.filter(status=True)


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer



class CustomLoginView(StandardResponseMixin, LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return self.success_response(data=response.data, user=request.user, status=status.HTTP_200_OK)
        else:
            return self.error_response(errors=response.errors, status=response.status_code)


class CustomRegisterView(RegisterView, StandardResponseMixin):
    def create(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return self.success_response(data=response.data, user=request.user, status=status.HTTP_201_CREATED)
        else:
            return self.error_response(errors=response.errors, status=response.status_code)

