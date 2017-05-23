from django.db.models import Q
from rest_framework import serializers, viewsets, permissions, pagination
from rest_api.utils import QueryParamApiView

from .models import Message, Chat

from application.api import register
from core.api import UserSerializer


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = 'id', 'text', 'chat'


class MessageViewSet(viewsets.ModelViewSet, QueryParamApiView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = permissions.IsAuthenticated,

    query_params = {
        'id': 'id',
        'chat': 'chat_id',
        'author': 'author_id'
    }

    def get_queryset(self):
        qs = super(MessageViewSet, self).get_queryset()
        qs = qs.filter(
            Q(author=self.request.user) |
            Q(chat__participants=self.request.user)
        )
        qs = qs.distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

register('messages', MessageViewSet)


class ChatSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    last_message = serializers.SerializerMethodField()

    def get_last_message(self, obj):
        # print(obj.messages.all())
        try:
            return MessageSerializer(obj.messages.latest('created')).data
        except:
            return None

    class Meta:
        model = Chat
        fields = 'id', 'participants', 'last_message'


class ChatViewSet(viewsets.ModelViewSet, QueryParamApiView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = permissions.IsAuthenticated,

    query_params = {
        'id': 'id',
        'author': 'author_id',
        'participant': 'participants'
    }

    def get_queryset(self):
        qs = super(ChatViewSet, self).get_queryset()
        qs = qs.filter(
            Q(author=self.request.user) |
            Q(participants=self.request.user)
        )
        qs = qs.distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


register('chats', ChatViewSet)
