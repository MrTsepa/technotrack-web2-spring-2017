from django.db.models.signals import post_save, post_delete


class Achievement:
    name = None
    model = None  # object of this type is checked with business logic
    observed_model = None   # saving something of this type initiates checks, by default is same as model
    title = None
    description = None

    def __init__(self):
        pass

    @classmethod
    def check_for(cls, instance):
        raise NotImplementedError

    @classmethod
    def get_achievable(cls, instance):
        raise NotImplementedError

    @classmethod
    def get_model_instance_for_observed_model(cls, instance):
        if cls.observed_model is None:
            return instance
        else:
            raise NotImplementedError


def register(achievement_class):
    from .models import Achievement
    a, created = Achievement.objects.get_or_create(
        name=achievement_class.name,
        defaults={
            'title': achievement_class.title,
            'description': achievement_class.description,
        }
    )

    def check_achievement(instance, *args, **kwargs):
        model_instance = achievement_class.get_model_instance_for_observed_model(instance)
        achievable = achievement_class.get_achievable(model_instance)
        check_res = achievement_class.check_for(model_instance)
        if check_res and a not in achievable.achievements.all():
            achievable.achievements.add(a)
        if not check_res and a in achievable.achievements.all():
            achievable.achievements.remove(a)

    post_save.connect(check_achievement, sender=achievement_class.observed_model, weak=False)
    post_delete.connect(check_achievement, sender=achievement_class.observed_model, weak=False)

    return achievement_class
