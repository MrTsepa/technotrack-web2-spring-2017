from rest_framework import serializers, viewsets, permissions, pagination

from .models import Message, Chat

from application.api import register


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = 'id', 'text', 'chat'


class Pagination(pagination.PageNumberPagination):
    page_size = 10


class CanViewMessage(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user in obj.chat.participants.all() or request.user == obj.author


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = permissions.IsAuthenticated, CanViewMessage
    pagination_class = Pagination

    def get_queryset(self):
        qs = super(MessageViewSet, self).get_queryset()

        if self.request.query_params.get('chat'):
            qs = qs.filter(chat_id=self.request.query_params.get('chat'))

        if self.suffix == u'List':
            ids = [obj.id for obj in qs if self.has_object_permission(self.request, obj)]
            qs = qs.filter(id__in=ids)
        return qs

    def has_object_permission(self, request, obj):
        for permission in self.get_permissions():
            if not permission.has_object_permission(request, self, obj):
                return False
        return True

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

register('messages', MessageViewSet)


class IsParticipant(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all() or request.user == obj.author


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = 'id', 'participants',


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = permissions.IsAuthenticated, IsParticipant

    def get_queryset(self):
        qs = super(ChatViewSet, self).get_queryset()
        if self.suffix == u'List':
            ids = [obj.id for obj in qs if self.has_object_permission(self.request, obj)]
            qs = qs.filter(id__in=ids)
        return qs

    def has_object_permission(self, request, obj):
        for permission in self.get_permissions():
            if not permission.has_object_permission(request, self, obj):
                return False
        return True

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


register('chats', ChatViewSet)
