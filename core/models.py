from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

from application import settings


class User(AbstractUser):

    pass


class Authored(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True


class Dated(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
