from django.db import models
from taggit.managers import TaggableManager

from bookworm.books.data.models import Book, BookList
from bookworm.core.data.models import AbstractModel


class BookListItem(AbstractModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_list = models.ForeignKey(BookList, on_delete=models.CASCADE)
    line_item = models.PositiveIntegerField(default=0)
    tags = TaggableManager()

