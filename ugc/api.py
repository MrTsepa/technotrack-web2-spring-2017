from rest_framework import serializers, viewsets, permissions
from .models import Post

from application.api import register


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = 'id', 'text'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = permissions.IsAuthenticated,

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

register('posts', PostViewSet)
