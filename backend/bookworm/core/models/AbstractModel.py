import uuid as uuid

from django.db import models


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4)
    deleted_timestamp = models.DateTimeField(null=True, blank=True)
    archived_timestamp = models.DateTimeField(null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
