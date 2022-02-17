from django.db import models


class AbstractLikeableModel(models.Model):
    class Meta:
        abstract = True

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
