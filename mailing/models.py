from __future__ import unicode_literals

from django.db import models

# Create your models here.
from application import settings


class MailingList(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name
