from __future__ import unicode_literals

from django.db import models

from core.models import Authored, Dated


class Post(Authored, Dated):
    text = models.TextField()