from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated


class Chat(Authored):
    participants = models.ManyToManyField("core.User", related_name="chats")

    def __unicode__(self):
        return u'Chat, id: %d' % self.id


class Message(Authored, Dated):
    text = models.TextField()
    chat = models.ForeignKey(Chat, related_name="messages")

    def __unicode__(self):
        return u'Message, id: %d, chat: %d' % (self.id, self.chat.id)
