from rest_framework import serializers

from bookworm.books.data.models import Author
from bookworm.core.data.serializers.BaseSerializer import BaseSerializer


class AuthorSerializer(BaseSerializer):
    first_name = serializers.CharField(max_length=255, min_length=1)
    last_name = serializers.CharField(max_length=255, min_length=1)
    full_name = serializers.CharField(max_length=255, min_length=2, read_only=True, required=False)

    class Meta:
        model = Author
        fields = ['uuid', 'first_name', 'last_name', 'full_name', 'created_timestamp', 'modified_timestamp']
        # read_only_field = ['uuid', 'created_timestamp', 'modified_timestamp']
