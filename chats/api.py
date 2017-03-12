from rest_framework import serializers, viewsets, permissions
from .models import Message

from application.api import register


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = 'id', 'text',


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = permissions.IsAuthenticated,

register('messages', MessageViewSet)
