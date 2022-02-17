from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex', write_only=True, required=False)

    deleted_timestamp = serializers.DateTimeField(required=False)
    archived_timestamp = serializers.DateTimeField(required=False)
    created_timestamp = serializers.DateTimeField(required=False)
    modified_timestamp = serializers.DateTimeField(required=False)
