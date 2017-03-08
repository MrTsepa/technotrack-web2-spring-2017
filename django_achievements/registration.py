from django.db.models.signals import post_save, post_delete


class Achievement:
    name = None

    '''object of this type is checked with business logic'''
    model = None

    '''saving something of this type initiates checks, by default is same as model'''
    observed_model = None

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


def check_and_give_achievement(achievement_class, model_instance):
    from .models import Achievement
    achievement_object = Achievement.objects.get(name=achievement_class.name)

    achievable = achievement_class.get_achievable(model_instance)
    check_res = achievement_class.check_for(model_instance)
    if check_res and achievement_object not in achievable.achievements.all():
        achievable.achievements.add(achievement_object)
    if not check_res and achievement_object in achievable.achievements.all():
        achievable.achievements.remove(achievement_object)


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
        check_and_give_achievement(achievement_class, model_instance)

    post_save.connect(
        check_achievement,
        sender=achievement_class.observed_model,
        weak=False,
        dispatch_uid=achievement_class.name + '_save'
    )
    post_delete.connect(
        check_achievement,
        sender=achievement_class.observed_model,
        weak=False,
        dispatch_uid=achievement_class.name + '_delete'
    )

    for model_instance in achievement_class.model.objects.all():
        check_and_give_achievement(achievement_class, model_instance)

    return achievement_class


def unregister(achievement_class):
    from .models import Achievement
    Achievement.objects.get(name=achievement_class.name).delete()
    post_save.disconnect(
        sender=achievement_class.observed_model,
        dispatch_uid=achievement_class.name + '_save'
    )
    post_delete.disconnect(
        sender=achievement_class.observed_model,
        dispatch_uid=achievement_class.name + '_delete'
    )


def unregister_all_achievements():
    from .models import Achievement
    for a in Achievement.objects.all():
        unregister(a)