from rest_framework import serializers
from timeline.models import Message


class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = ('id', 'created', 'data')