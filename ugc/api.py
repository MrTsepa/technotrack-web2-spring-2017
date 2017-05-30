from rest_framework import serializers, viewsets, permissions

from .models import Post

from core.api import UserSerializer

from application.api import register


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = 'id', 'text', 'title'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = permissions.IsAuthenticated,

    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()
        if self.request.query_params.get('user'):
            qs = qs.filter(author_id=self.request.query_params.get('user'))
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

register('posts', PostViewSet)
