from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ts_generator.Route import route

from bookworm.books.data.serializers import AuthorSerializer
from bookworm.books.data.models import Author


@route('author', name='author', method=['get', 'post', 'delete', 'put'])
class AuthorViewSet(viewsets.ViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request):
        authors = self.queryset
        return Response(authors)

    def list(self, request, **kwargs):
        serializer = AuthorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = AuthorSerializer(user)
        return Response(serializer.data)
