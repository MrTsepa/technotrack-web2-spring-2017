from django_achievements.registration import Achievement, register
from likes.models import Like
from ugc.models import Post
from .models import User


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
        assert isinstance(instance, cls.get_observed_model())
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
        assert isinstance(observed_model_instance, cls.get_observed_model())
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
