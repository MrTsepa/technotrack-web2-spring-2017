from django.db.models.signals import post_save

from core.models import Authored
from feed.models import Feedable, CreationEvent


def create_event_on_creation(instance, created=False, *args, **kwargs):
    if created:
        if isinstance(instance, Authored):
            CreationEvent.objects.create(created_object=instance, author=instance.author)
        else:
            print "Can't create event for not authored instance"


for subclass in Feedable.__subclasses__():
    post_save.connect(create_event_on_creation, sender=subclass)
