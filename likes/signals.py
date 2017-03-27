from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch.dispatcher import receiver

from likes.models import Like


def increase_likescount(instance, created=False, *args, **kwargs):
    if created:
        instance.target.likescount += 1
    else:
        instance.target.likescount = instance.target.likes.count()
    instance.target.save()


def decrease_likescount(instance, *args, **kwargs):
    instance.target.likescount = instance.target.likes.count()
    instance.target.save()

post_save.connect(increase_likescount, sender=Like)

post_delete.connect(decrease_likescount, sender=Like)


@receiver(pre_save, sender=Like)
def clean(instance, *args, **kwargs):
    instance.full_clean()
