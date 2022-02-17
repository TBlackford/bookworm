from rest_framework import serializers

from bookworm.books.data.models import Author
from bookworm.core.data.serializers.BaseSerializer import BaseSerializer


class AuthorSerializer(BaseSerializer):
    first_name = serializers.CharField(max_length=255, min_length=1)
    last_name = serializers.CharField(max_length=255, min_length=1)
    full_name = serializers.CharField(max_length=255, min_length=2, read_only=True, required=False)

    def create(self, validated_data):
        return super().create(self, validated_data=validated_data)

    class Meta:
        depth = 1
        model = Author
        #fields = '__all__'
        exclude = ['id']
