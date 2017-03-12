from rest_framework import serializers, viewsets, permissions
from .models import CreationEvent

from application.api import register


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreationEvent
        fields = 'id',


class EventViewSet(viewsets.ModelViewSet):
    queryset = CreationEvent.objects.all()
    serializer_class = EventSerializer
    permission_classes = permissions.IsAuthenticated,

register('events', EventViewSet)
