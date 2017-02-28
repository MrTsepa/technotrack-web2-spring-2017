from django.db.models.signals import post_save

from feed.models import Feedable, CreationEvent


def create_event_on_creation(instance, created=False, *args, **kwargs):
    if created:
        CreationEvent.objects.create(created_object=instance)

for subclass in Feedable.__subclasses__():
    post_save.connect(create_event_on_creation, sender=subclass)
