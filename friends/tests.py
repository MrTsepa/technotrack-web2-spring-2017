from django.test import TestCase

from core.models import User
from friends.models import Friendship, Friend


class FriendshipTestCase(TestCase):
    def setUp(self):
        pass

    def test_friend_created(self):
        u1 = User.objects.create(username='u1')
        u2 = User.objects.create(username='u2')
        f = Friendship.objects.create(author=u1, recipient=u2)

        self.assertEqual(u1.friends.all().count(), 0)
        self.assertEqual(u2.friends.all().count(), 0)
        f.approved = True
        f.save()
        self.assertEqual(Friend.objects.count(), 2)
        self.assertEqual(u1.friends.filter(user2=u2).count(), 1)
        self.assertEqual(u2.friends.filter(user2=u1).count(), 1)

    def test_friend_removed(self):
        u1 = User.objects.create(username='u1')
        u2 = User.objects.create(username='u2')
        f = Friendship.objects.create(author=u1, recipient=u2)

        f.approved = True
        f.save()
        f.approved = False
        f.save()
        self.assertEqual(Friend.objects.count(), 0)
        self.assertEqual(u1.friends.all().count(), 0)
        self.assertEqual(u2.friends.all().count(), 0)

    def tearDown(self):
        pass
