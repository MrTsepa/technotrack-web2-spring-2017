from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import Dated, Authored


class CreationEvent(Dated, Authored):
    created_object = GenericForeignKey(ct_field='object_content_type', fk_field='object_id')
    object_content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()


class Feedable(models.Model):
    creation_events = GenericRelation(
        CreationEvent,
        content_type_field='object_content_type',
        object_id_field='object_id'
    )

    class Meta:
        abstract = True
