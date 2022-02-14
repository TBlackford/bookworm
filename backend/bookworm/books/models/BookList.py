from django.db import models

from bookworm.books.models import Author
from bookworm.core.models import AbstractModel


class BookList(AbstractModel):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_private = models.BooleanField()
