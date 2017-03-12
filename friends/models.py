from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated, User
from feed.models import Feedable
from likes.models import Likable


class Friendship(Feedable, Authored, Dated, Likable):
    recipient = models.ForeignKey("core.User")
    approved = models.BooleanField(default=False)


class Friend(models.Model):
    user1 = models.ForeignKey("core.User", related_name="friends")
    user2 = models.ForeignKey("core.User", related_name="+")
