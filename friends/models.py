from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated, User
from feed.models import Feedable


class Friendship(Authored, Dated, Feedable):
    recipient = models.ForeignKey("core.User")
    approved = models.BooleanField(default=False)


class Friend(models.Model):
    user1 = models.ForeignKey("core.User", related_name="+")
    user2 = models.ForeignKey("core.User")
