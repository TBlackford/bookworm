from django.http import QueryDict
from rest_framework import viewsets
from rest_framework.response import Response

from ts_generator.Route import route

from bookworm.books.data.serializers import BookSerializer
from bookworm.books.data.models import Book, Author


@route('book', name='book', method=['get', 'post', 'delete', 'put'])
class BookViewSet(viewsets.ViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request):
        serializers = [BookSerializer(book, many=True) for book in self.queryset]
        return Response(serializers)

    def list(self, request, **kwargs):
        serializer = BookSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        print(request.data)
        print(kwargs)
        data: QueryDict = request.data
        author_id = data.pop('author')[0]
        author = Author.objects.get(pk=author_id)
        book = Book.objects.create(**{
            'title': data.pop('title')[0],
            'isbn': data.pop('isbn')[0],
            'pages': data.pop('pages')[0],
            'format': data.pop('format')[0],
            'language': data.pop('language')[0],
            'pub_date': data.pop('pub_date')[0],
            'first_pub_date': data.pop('first_pub_date')[0],
            'rating': data.pop('rating')[0],
        }, author=author)

        book.save()

        return Response({
            'modified_timestamp': book.modified_timestamp
        })

    def destroy(self, request, pk=None):
        author = Book.objects.get(uuid=pk)
        author.delete()

        return Response({
            'modified_timestamp': author.modified_timestamp
        })