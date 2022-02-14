from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ts_generator.Route import route

from bookworm.books.interfaces.serializers import AuthorSerializer
from bookworm.books.models import Author


@route('author', name='author', method=['get', 'post', 'delete', 'put'])
class AuthorViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(user)
        return Response(serializer.data)
