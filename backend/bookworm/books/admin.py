from django.contrib import admin

# Register your models here.
from bookworm.books.data.models import Author, Book, BookList, BookListItem, Review

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookList)
admin.site.register(BookListItem)
admin.site.register(Review)
