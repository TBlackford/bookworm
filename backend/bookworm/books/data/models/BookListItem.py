from django.db import models

from bookworm.books.data.models.Book import Book
from bookworm.core.data.models import AbstractModel


class BookListItem(AbstractModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    line_item = models.IntegerField(default=0)
