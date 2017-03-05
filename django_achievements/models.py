from __future__ import unicode_literals

from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return 'name: ' + self.name


class Achievable(models.Model):
    achievements = models.ManyToManyField(Achievement, editable=False)

    class Meta:
        abstract = True
