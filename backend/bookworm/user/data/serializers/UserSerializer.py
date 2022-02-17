from rest_framework import serializers

from bookworm.user.data.models import AppUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        name = 'Details'
        model = AppUser
        fields = ['uuid', 'username', 'email', 'is_active', 'created_timestamp', 'modified_timestamp']
        read_only_field = ['uuid', 'is_active', 'created_timestamp', 'modified_timestamp']
