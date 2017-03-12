from rest_framework import serializers, viewsets, permissions
from .models import User

from application.api import register


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'id', 'username',


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.IsAuthenticated,

register('users', UserViewSet)
