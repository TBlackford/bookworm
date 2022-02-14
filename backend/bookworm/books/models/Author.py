from django.db import models
from django.forms import ModelForm

from bookworm.core.models import AbstractModel


class Author(AbstractModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
