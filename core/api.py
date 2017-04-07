from rest_framework import serializers, viewsets, permissions

from .models import User

from application.api import register


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'id', 'username',
        read_only_fields = 'username',


class FullUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
            "achievements",
        )
        read_only_fields = (
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions"
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = permissions.IsAuthenticated,

    def get_serializer_class(self):
        if self.suffix == u'List':
            return UserSerializer

        if self.get_object() == self.request.user:
            return FullUserSerializer
        else:
            return UserSerializer

register('users', UserViewSet)
