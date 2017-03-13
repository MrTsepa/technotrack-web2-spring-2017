from rest_framework import serializers, viewsets, permissions
from rest_framework.reverse import reverse

from .models import CreationEvent

from application.api import register


class EventSerializer(serializers.ModelSerializer):
    created_object = serializers.SerializerMethodField()

    def get_created_object(self, obj):
        viewname = '%s-detail' % obj.object_content_type.name
        return reverse(viewname, (obj.object_id,))

    class Meta:
        model = CreationEvent
        fields = 'id', 'created_object'


class EventViewSet(viewsets.ModelViewSet):
    queryset = CreationEvent.objects.all()
    serializer_class = EventSerializer
    permission_classes = permissions.IsAuthenticated,
    http_method_names = ['get']

register('events', EventViewSet)
