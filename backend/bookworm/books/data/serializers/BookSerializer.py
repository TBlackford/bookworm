from rest_framework import serializers

from bookworm.books.data.models import Book
from bookworm.books.data.serializers import AuthorSerializer
from bookworm.core.data.serializers.BaseSerializer import BaseSerializer


class BookSerializer(BaseSerializer):
    title = serializers.CharField(max_length=255)
    author = AuthorSerializer()

    isbn = serializers.CharField(max_length=255)
    pages = serializers.IntegerField(default=0)
    format = serializers.CharField(max_length=2)
    language = serializers.CharField(max_length=2)

    pub_date = serializers.DateTimeField('date published')
    first_pub_date = serializers.DateTimeField('first date published')

    def create(self, validated_data):
        return super().create(self, validated_data)
    
    class Meta:
        depth = 1
        model = Book
        exclude = ['id']
