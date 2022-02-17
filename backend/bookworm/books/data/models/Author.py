import uuid
from datetime import datetime

from django.db import models
from django.forms import ModelForm

from bookworm.core.data.models import AbstractModel


class Author(AbstractModel):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def create(self, validated_data):
        now = datetime.now()
        self.uuid = uuid.UUID()
        self.created_timestamp = now
        self.modified_timestamp = now
        print('new author model', self)
        return validated_data

    # def delete(self, using=None, keep_parents=False):
    #     now = datetime.now()
    #     self.created_timestamp = now
    #     self.modified_timestamp = now

    def __str__(self):
        return self.full_name()


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
