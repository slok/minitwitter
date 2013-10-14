from django.db import models


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='messages')

    class Meta:
        ordering = ('created',)