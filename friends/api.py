from rest_framework import serializers, viewsets, permissions
from .models import Friendship

from application.api import register


class FriendshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friendship
        fields = 'recipient', 'approved'


class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
    permission_classes = permissions.IsAuthenticated,


register('friendships', FriendshipViewSet)
