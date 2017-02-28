from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from core.models import Authored, Dated
from feed.models import Feedable


class Like(Feedable, Authored, Dated):
    target = GenericForeignKey(ct_field='target_content_type', fk_field='target_id')
    target_content_type = models.ForeignKey(ContentType)
    target_id = models.PositiveIntegerField()

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + \
               'Author: ' + self.author.username


class Likable(models.Model):
    likes = GenericRelation(
        Like,
        content_type_field='target_content_type',
        object_id_field='target_id'
    )

    class Meta:
        abstract = True
