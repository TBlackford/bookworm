from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from bookworm.user.data.serializers import AppUserSerializer


class LoginSerializer(TokenObtainPairSerializer):
    user = AppUserSerializer(many=False, required=False)
    refresh = serializers.CharField(max_length=128, min_length=8, write_only=True, required=False)
    access = serializers.CharField(max_length=128, min_length=8, write_only=True, required=False)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = AppUserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
