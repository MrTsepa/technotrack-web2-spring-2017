from django.test import TestCase

from core.models import User
from likes.models import Like
from ugc.models import Post


class LikesTestCase(TestCase):

    def test_likecount_increase(self):
        u1 = User.objects.create(username='u1')
        u2 = User.objects.create(username='u2')
        u3 = User.objects.create(username='u3')
        p = Post.objects.create(author=u1, text="aaa")
        p_id = p.id
        self.assertEqual(Post.objects.get(pk=p_id).likescount, 0)
        Like.objects.create(author=u2, target=p)
        self.assertEqual(Post.objects.get(pk=p_id).likescount, 1)
        Like.objects.create(author=u3, target=p)
        self.assertEqual(Post.objects.get(pk=p_id).likescount, 2)

    def test_likecount_decrease(self):
        u1 = User.objects.create(username='u1')
        u2 = User.objects.create(username='u2')
        u3 = User.objects.create(username='u3')
        p = Post.objects.create(author=u1, text="aaa")
        p_id = p.id
        Like.objects.create(author=u2, target=p)
        Like.objects.create(author=u3, target=p)
        self.assertEqual(Post.objects.get(pk=p_id).likescount, 2)
        p.likes.filter(author=u3).delete()
        self.assertEqual(Post.objects.get(pk=p_id).likescount, 1)
        p.likes.filter(author=u2).delete()
        self.assertEqual(Post.objects.get(pk=p_id).likescount, 0)

