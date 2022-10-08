from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    text = serializers.CharField()

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class EntryDetailSerializer(serializers.Serializer):
    message = MessageSerializer()
    user = UserSerializer()
