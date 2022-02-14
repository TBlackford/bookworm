from django.db import models

from bookworm.books.models.Book import Book
from bookworm.core.models import AbstractModel


class BookListItem(AbstractModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    line_item = models.IntegerField(default=0)
