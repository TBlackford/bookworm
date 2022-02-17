from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from bookworm.books.data.models import Author
from bookworm.core.data.models import AbstractModel, AbstractRateableModel


class Book(AbstractModel, AbstractRateableModel):
    class Language(models.TextChoices):
        BLANK = '--', _('----')
        ENGLISH = 'EN', _('English')
        GERMAN = 'DE', _('German')
        RUSSIAN = 'RU', _('Russian')

    class BookFormat(models.IntegerChoices):
        BLANK = 0, _('----')
        PAPERBACK = 1, _('PAPERBACK')
        HARDCOVER = 2, _('HARDCOVER')
        LEATHER_BOUND = 3, _('LEATHER_BOUND')

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    isbn = models.TextField()
    pages = models.PositiveIntegerField(default=0)
    format = models.IntegerField(choices=BookFormat.choices, default=BookFormat.BLANK)
    language = models.CharField(max_length=2, choices=Language.choices, default=Language.BLANK)

    tags = TaggableManager()

    pub_date = models.DateTimeField('date published', null=True)
    first_pub_date = models.DateTimeField('first date published', null=True)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date']
