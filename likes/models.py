from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from core.models import Authored, Dated
from feed.models import Feedable


class Like(Feedable, Authored, Dated):
    target = GenericForeignKey(ct_field='target_content_type', fk_field='target_id')
    target_content_type = models.ForeignKey(ContentType)
    target_id = models.PositiveIntegerField()

    def clean(self):
        for l in self.target.likes.all():
            if l.author == self.author:
                raise ValidationError("Like already exists.")

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + \
               'Author: ' + self.author.username


class Likable(models.Model):
    likes = GenericRelation(
        Like,
        content_type_field='target_content_type',
        object_id_field='target_id',
    )
    likescount = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        abstract = True
