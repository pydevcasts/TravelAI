from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from users.manager import UserManager



class CustomGroup(Group):
    
    min_participants = models.PositiveIntegerField(default=1)
    max_participants = models.PositiveIntegerField(default=10)
    status = models.BooleanField(default=True)  # True for active, False for inactive
    # class Meta:
    #     proxy = True
    def user_count(self):
        return self.users.count()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    group = models.ForeignKey(CustomGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.username


class Trip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    available_seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')  # active, inactive

    def __str__(self):
        return f"{self.user.username} - {self.destination} at {self.departure_time}"

class Request(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')  # pending, accepted, rejected
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Request by {self.user.username} for {self.trip.destination}"

class Rating(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField()  # 1 to 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating by {self.user.username} for {self.trip.destination}: {self.score}"
