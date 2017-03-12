from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated


class Chat(Authored):
    participants = models.ManyToManyField("core.User")


class Message(Authored, Dated):
    text = models.TextField()
    chat = models.ForeignKey(Chat, related_name="messages_related")
