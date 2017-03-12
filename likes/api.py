from rest_framework.reverse import reverse
from rest_framework import serializers, viewsets, permissions
from .models import Like

from application.api import register


class LikeSerializer(serializers.ModelSerializer):
    target = serializers.SerializerMethodField('get_target_hyperlink_field')

    def get_target_hyperlink_field(self, obj):
        viewname = '%s-detail' % obj.target_content_type.name
        return reverse(viewname, (obj.target_id,))

    class Meta:
        model = Like
        fields = 'target',


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = permissions.IsAuthenticated,

register('likes', LikeViewSet)
