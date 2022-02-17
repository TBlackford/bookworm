from rest_framework import viewsets
from rest_framework.response import Response

from ts_generator.Route import route

from bookworm.books.data.serializers import AuthorSerializer
from bookworm.books.data.models import Author


@route('author', name='author', method=['get', 'post', 'delete', 'put'])
class AuthorViewSet(viewsets.ViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request):
        serializers = [AuthorSerializer(author, many=True) for author in self.queryset]
        return Response(serializers)

    def list(self, request, **kwargs):
        serializer = AuthorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        author = Author.objects.get(uuid=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        author = Author.objects.create()
        author.first_name = request.data['first_name']
        author.last_name = request.data['last_name']
        author.save()

        return Response({
            'modified_timestamp': author.modified_timestamp
        })

    def destroy(self, request, pk=None):
        author = Author.objects.get(uuid=pk)
        author.delete()

        return Response({
            'modified_timestamp': author.modified_timestamp
        })

