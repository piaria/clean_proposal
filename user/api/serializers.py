from rest_framework import serializers
from pydantic import BaseModel

class UserDetailSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)