from django.test import TestCase

from core.models import User
from django_achievements.registration import register, unregister, unregister_all_achievements
from likes.models import Like
from ugc.models import Post
from .models import AchievementModel
from .registration import Achievement


class PostCountAchievementTestCase(TestCase):
    def setUp(self):
        class PostCountAchievement(Achievement):
            model = User
            count = None
            observed_model = Post

            @classmethod
            def check_for(cls, instance):
                assert isinstance(instance, User)
                return instance.ugc_post_related.count() >= cls.count

            @classmethod
            def get_achievable(cls, instance):
                assert isinstance(instance, User)
                return instance

            @classmethod
            def get_model_instance_for_observed_model(cls, instance):
                assert isinstance(instance, cls.observed_model)
                return instance.author

        @register
        class Post1(PostCountAchievement):
            name = "1_post"
            count = 1
            title = "1 Post"
            description = "You've published 1 post"

        @register
        class Post10(PostCountAchievement):
            name = "10_posts"
            count = 10
            title = "10 Posts"
            description = "You've published 10 posts"

        @register
        class Post100(PostCountAchievement):
            name = "100_posts"
            count = 100
            title = "100 Posts"
            description = "You've published 100 posts"

        self.Post1 = Post1
        self.Post10 = Post10
        self.Post100 = Post100

    def test_achievement_added(self):
        u1 = User.objects.create(username='u1')
        u1_id = u1.id
        a1 = AchievementModel.objects.get(name='1_post')
        a10 = AchievementModel.objects.get(name='10_posts')
        a100 = AchievementModel.objects.get(name='100_posts')

        for i in range(1, 110):
            Post.objects.create(author=u1)
            achievements = User.objects.get(pk=u1_id).achievements.all()
            if i < 10:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 not in achievements)
                self.assertTrue(a100 not in achievements)
            elif i < 100:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 not in achievements)
            else:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 in achievements)

    def test_achievement_removed(self):
        u1 = User.objects.create(username='u1')
        u1_id = u1.id

        a1 = AchievementModel.objects.get(name='1_post')
        a10 = AchievementModel.objects.get(name='10_posts')
        a100 = AchievementModel.objects.get(name='100_posts')

        for _ in range(1, 110):
            Post.objects.create(author=u1)
        for _ in range(1, 110):
            Post.objects.filter(author=u1)[0].delete()
            achievements = User.objects.get(pk=u1_id).achievements.all()
            i = Post.objects.filter(author=u1).count()
            if i == 0:
                self.assertTrue(a1 not in achievements)
                self.assertTrue(a10 not in achievements)
                self.assertTrue(a100 not in achievements)
            elif i < 10:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 not in achievements)
                self.assertTrue(a100 not in achievements)
            elif i < 100:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 not in achievements)
            else:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 in achievements)

    def tearDown(self):
        unregister(self.Post1)
        unregister(self.Post10)
        unregister(self.Post100)


class LikeCountAchievementTestCase(TestCase):
    def setUp(self):
        class LikeCountAchievement(Achievement):
            model = Post
            count = None
            observed_model = Like

            @classmethod
            def check_for(cls, instance):
                assert isinstance(instance, cls.model)
                return instance.likescount >= cls.count

            @classmethod
            def get_achievable(cls, instance):
                assert isinstance(instance, cls.model)
                return instance.author

            @classmethod
            def get_model_instance_for_observed_model(cls, observed_model_instance):
                assert isinstance(observed_model_instance, cls.observed_model)
                return observed_model_instance.target

        @register
        class Like1(LikeCountAchievement):
            name = "1_like"
            count = 1
            title = "1 Like"
            description = "You've post has 1 like"

        @register
        class Like10(LikeCountAchievement):
            name = "10_likes"
            count = 10
            title = "10 Likes"
            description = "You've post has 10 likes"

        @register
        class Like100(LikeCountAchievement):
            name = "100_likes"
            count = 100
            title = "100 Likes"
            description = "You've post has 100 likes"

        self.Like1 = Like1
        self.Like10 = Like10
        self.Like100 = Like100

    def test_achievement_added(self):
        u1 = User.objects.create(username='admin')
        u1_id = u1.id
        p = Post.objects.create(author=u1, text='aaaaaa')

        users = []
        for i in range(120):
            users.append(User.objects.create(username='u'+str(i)))

        a1 = AchievementModel.objects.get(name='1_like')
        a10 = AchievementModel.objects.get(name='10_likes')
        a100 = AchievementModel.objects.get(name='100_likes')

        self.assertTrue(a1 not in u1.achievements.all())
        self.assertTrue(a10 not in u1.achievements.all())
        self.assertTrue(a100 not in u1.achievements.all())

        for user in users:
            Like.objects.create(author=user, target=p)
            i = p.likes.count()
            achievements = User.objects.get(pk=u1_id).achievements.all()

            if i < 10:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 not in achievements)
                self.assertTrue(a100 not in achievements)
            elif i < 100:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 not in achievements)
            else:
                self.assertTrue(a1 in achievements)
                self.assertTrue(a10 in achievements)
                self.assertTrue(a100 in achievements)

    def tearDown(self):
        unregister(self.Like1)
        unregister(self.Like10)
        unregister(self.Like100)
