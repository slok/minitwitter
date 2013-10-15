from django.contrib.auth.models import User
from rest_framework import serializers

from timeline.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail')
    lookup_field='pk',

    class Meta:
        model = Message
        fields = ('id', 'created', 'data', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    messages = serializers.HyperlinkedRelatedField(many=True, view_name='message-detail')
    lookup_field='pk',

    class Meta:
        model = User
        fields = ('id', 'username', 'messages')