from rest_framework import serializers


class MessageDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    user_id = serializers.IntegerField()
    timestamp = serializers.DateTimeField()


class MessageCreationSerializer(serializers.Serializer):
    text = serializers.CharField()
    user_id = serializers.IntegerField()
