from __future__ import unicode_literals

from django.db import models

from core.models import Authored, Dated
from feed.models import Feedable
from likes.models import Likable


class Post(Feedable, Authored, Dated, Likable):
    text = models.TextField()

    def __str__(self):
        return 'Post, ' 'id: ' + str(self.id) + ', ' + \
               'Author: ' + self.author.username
