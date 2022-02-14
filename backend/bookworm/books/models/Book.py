from django.db import models
from django.forms import ModelForm

from bookworm.books.models import Author
from bookworm.core.models import AbstractModel


class Book(AbstractModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    likes = models.IntegerField(default=0)

    pub_date = models.DateTimeField('date published')


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date']
