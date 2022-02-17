from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from bookworm.user.data.serializers import UserSerializer
from bookworm.user.data.models import AppUser


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = AppUser
        fields = ['uuid', 'username', 'email', 'password', 'is_active']

    def create(self, validated_data):
        try:
            user = AppUser.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = AppUser.objects.create_user(**validated_data)
        return user
