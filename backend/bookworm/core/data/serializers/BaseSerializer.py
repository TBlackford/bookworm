import uuid
from datetime import datetime

from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex', read_only=True, required=False)

    deleted_timestamp = serializers.DateTimeField(required=False, read_only=True)
    archived_timestamp = serializers.DateTimeField(required=False, read_only=True)
    created_timestamp = serializers.DateTimeField(required=False, read_only=True)
    modified_timestamp = serializers.DateTimeField(required=False, read_only=True)

    def create(self, validated_data):
        self.uuid = uuid.UUID()
        self.created_timestamp = datetime.now()
        print('new author serializer', self)
        return validated_data
