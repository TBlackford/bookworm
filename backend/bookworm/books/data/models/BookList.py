from django.db import models

from bookworm.core.data.models import AbstractModel, AbstractLikeableModel


class BookList(AbstractModel, AbstractLikeableModel):
    name = models.CharField(max_length=255)
    is_private = models.BooleanField()
