
from rest_framework import serializers
from .models import CustomUser,  CustomGroup, Rating, Request, Trip

class GroupSerializer(serializers.ModelSerializer):
    user_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomGroup
        fields = ['id', 'name', 'user_count']

    def get_user_count(self, obj):
        return obj.user.count()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'group', 'password']

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.group = validated_data.get('group', instance.group)
        instance.save()
        return instance


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'user', 'destination', 'departure_time', 'available_seats', 'status', 'created_at']

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'trip', 'user', 'status', 'created_at', 'notes']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'trip', 'user', 'score', 'comment', 'created_at']