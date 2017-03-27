from rest_framework import routers

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
            viewset.serializer_class.Meta.fields += 'likescount',
            viewset.serializer_class.Meta.read_only_fields += 'likescount',

    router.register(name, viewset)
