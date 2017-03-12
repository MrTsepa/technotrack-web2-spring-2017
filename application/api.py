from rest_framework import routers
from rest_framework import serializers

from core.models import Authored, Dated
from likes.models import Likable

router = routers.DefaultRouter()


def register(name, viewset):
    model = viewset.serializer_class.Meta.model

    if issubclass(model, Authored):
        viewset.serializer_class.author = serializers.ReadOnlyField(source='author_id')
        viewset.serializer_class.Meta.fields += 'author',

    if issubclass(model, Dated):
        viewset.serializer_class.Meta.fields += 'created', 'updated',

    if issubclass(model, Likable):
        viewset.serializer_class.Meta.fields += 'likescount',

    router.register(name, viewset)
