from django.db.models.signals import post_save

from friends.models import Friendship, Friend


def create_friends_on_friendship_approved(instance, *args, **kwargs):
    if isinstance(instance, Friendship):
        user1 = instance.author
        user2 = instance.recipient
        if instance.approved:
            if user2 not in user1.friends.all():
                Friend.objects.create(user1=user1, user2=user2)
            if user1 not in user2.friends.all():
                Friend.objects.create(user1=user2, user2=user1)
        else:
            if Friend.objects.filter(user1=user1, user2=user2):
                Friend.objects.get(user1=user1, user2=user2).delete()
            if Friend.objects.filter(user1=user2, user2=user1):
                Friend.objects.get(user1=user2, user2=user1).delete()


post_save.connect(create_friends_on_friendship_approved, sender=Friendship)
