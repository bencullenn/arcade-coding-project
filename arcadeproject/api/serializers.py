from rest_framework import serializers


class KeyValueSerializer(serializers.Serializer):
    key = serializers.CharField(required=True)
    value = serializers.CharField(required=True)


class KeySerializer(serializers.Serializer):
    key = serializers.CharField(required=True)


class TransactionSerializer(serializers.Serializer):
    # Empty serializer for transaction operations that don't require data
    pass
