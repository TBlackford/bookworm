from rest_framework import serializers

from bookworm.books.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        name = 'Details'
        model = Author
        fields = ['first_name', 'last_name', 'full_name', 'created_timestamp', 'modified_timestamp']
        read_only_field = ['uuid', 'created_timestamp', 'modified_timestamp']
