from rest_framework import routers
from rest_framework import serializers

from core.models import Authored, Dated
from likes.models import Likable

router = routers.DefaultRouter()


def register(name, viewset):
    if viewset.serializer_class is not None:

        model = viewset.serializer_class.Meta.model

        if not hasattr(viewset.serializer_class.Meta, 'read_only_fields'):
            viewset.serializer_class.Meta.read_only_fields = ()

        if issubclass(model, Authored):
            viewset.serializer_class.Meta.fields += 'author',
            viewset.serializer_class.Meta.read_only_fields += 'author',

        if issubclass(model, Dated):
            viewset.serializer_class.Meta.fields += 'created', 'updated',
            viewset.serializer_class.Meta.read_only_fields += 'created', 'updated',

        if issubclass(model, Likable):
            from likes.api import LikeSerializer

            class C(viewset.serializer_class):
                likes = LikeSerializer(many=True, read_only=True)
            viewset.serializer_class = C

            viewset.serializer_class.Meta.fields += 'likes', 'likescount',
            viewset.serializer_class.Meta.read_only_fields += 'likes', 'likescount',

    router.register(name, viewset)
