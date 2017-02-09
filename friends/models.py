from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated


class Friendship(Authored, Dated):
    recipient = models.ForeignKey("core.User")
    approved = models.BooleanField(default=False)


class Friend(models.Model):
    user1 = models.ForeignKey("core.User", related_name="+")
    user2 = models.ForeignKey("core.User", related_name="+")
