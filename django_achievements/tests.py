from django.test import TestCase

from core.models import User
from django_achievements.utils import register
from likes.models import Like
from ugc.models import Post
from .models import Achievement


class PostCountAchievementTestCase(TestCase):
    def setUp(self):
        from core.achievements import Post1, Post10, Post100
        register(Post1)
        register(Post10)
        register(Post100)

    def test_achievement_added(self):
        u1 = User.objects.create(username='u1')
        u1_id = u1.id
        a1 = Achievement.objects.get(name='1_post')
        a10 = Achievement.objects.get(name='10_posts')
        a100 = Achievement.objects.get(name='100_posts')

        self.assertEqual(u1.achievements.count(), 0)

        for i in range(1, 110):
            Post.objects.create(author=u1)
            achievements = User.objects.get(pk=u1_id).achievements.all()
            if i < 10:
                self.assertEqual(achievements.count(), 1)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 not in achievements)
                self.assertTrue(a100 not in achievements)
            elif i < 100:
                self.assertEqual(achievements.count(), 2)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 not in achievements)
            else:
                self.assertEqual(achievements.count(), 3)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 in achievements)

    def test_achievement_removed(self):
        u1 = User.objects.create(username='u1')
        u1_id = u1.id

        a1 = Achievement.objects.get(name='1_post')
        a10 = Achievement.objects.get(name='10_posts')
        a100 = Achievement.objects.get(name='100_posts')

        for _ in range(1, 110):
            Post.objects.create(author=u1)
        for _ in range(1, 110):
            Post.objects.filter(author=u1)[0].delete()
            achievements = User.objects.get(pk=u1_id).achievements.all()
            i = Post.objects.filter(author=u1).count()
            if i == 0:
                self.assertEqual(achievements.count(), 0)
                self.assertTrue(a1 not in achievements)
                self.assertTrue(a10 not in achievements)
                self.assertTrue(a100 not in achievements)
            elif i < 10:
                self.assertEqual(achievements.count(), 1)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 not in achievements)
                self.assertTrue(a100 not in achievements)
            elif i < 100:
                self.assertEqual(achievements.count(), 2)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 not in achievements)
            else:
                self.assertEqual(achievements.count(), 3)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 in achievements)


class LikeCountAchievementTestCase(TestCase):
    def setUp(self):
        from core.achievements import Like1, Like10, Like100
        register(Like1)
        register(Like10)
        register(Like100)

    def test_achievement_added(self):
        u1 = User.objects.create(username='admin')
        u1_id = u1.id
        p = Post.objects.create(author=u1, text='aaaaaa')

        users = []
        for i in range(120):
            users.append(User.objects.create(username='u'+str(i)))

        a1 = Achievement.objects.get(name='1_like')
        a10 = Achievement.objects.get(name='10_likes')
        a100 = Achievement.objects.get(name='100_likes')

        self.assertEqual(u1.achievements.count(), 0)

        for user in users:
            Like.objects.create(author=user, target=p)
            i = p.likes.count()
            achievements = User.objects.get(pk=u1_id).achievements.all()

            if i < 10:
                self.assertEqual(achievements.count(), 1)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 not in achievements)
                self.assertTrue(a100 not in achievements)
            elif i < 100:
                self.assertEqual(achievements.count(), 2)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 not in achievements)
            else:
                self.assertEqual(achievements.count(), 3)
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 in achievements)
