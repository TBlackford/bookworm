from django.db import models

from bookworm.core.data.models import AbstractModel
from bookworm.user.data.models import AppUser


class Review(AbstractModel):
    text = models.TextField()
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    # Votes
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)