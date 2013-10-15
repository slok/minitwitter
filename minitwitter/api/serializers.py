from rest_framework import serializers
from timeline.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'created', 'data')