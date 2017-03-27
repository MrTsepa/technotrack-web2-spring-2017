from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework import serializers, viewsets, permissions

from ugc.models import Post
from .models import Like

from rest_api.utils import QueryParamApiView

from application.api import register


class LikeSerializer(serializers.ModelSerializer):
    target_type = serializers.SerializerMethodField()

    def get_target_type(self, obj):
        return obj.target_content_type.name

    class Meta:
        model = Like
        fields = 'id', 'target_type', 'target_id'


class LikeViewSet(viewsets.ModelViewSet, QueryParamApiView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = permissions.IsAuthenticated,

    query_params = {
        'target_type': 'target_content_type__model',  # maybe 'post' or 'friendship'
        'target': 'target_id'
    }

    def get_queryset(self):
        qs = super(LikeViewSet, self).get_queryset()
        post_id = self.request.query_params.get('post')
        if post_id is not None:
            qs = qs.filter(
                Q(target_content_type=ContentType.objects.get_for_model(Post)) &
                Q(target_id=post_id)
            )
        return qs

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            target_content_type=ContentType.objects.get_for_model(Post)
        )

register('likes', LikeViewSet)
