from django.db.models.signals import post_save, post_delete
from .models import AchievementModel


class Achievement:
    name = None  # must be unique

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
    achievement_object = AchievementModel.objects.get(name=achievement_class.name)

    achievable = achievement_class.get_achievable(model_instance)
    check_res = achievement_class.check_for(model_instance)
    if check_res and achievement_object not in achievable.achievements.all():
        achievable.achievements.add(achievement_object)
    if not check_res and achievement_object in achievable.achievements.all():
        achievable.achievements.remove(achievement_object)


class AlreadyRegistered(Exception):
    pass


class NotRegistered(Exception):
    pass


class AchievementRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, achievement_class):
        if achievement_class.name in self._registry:
            raise AlreadyRegistered

        self._registry[achievement_class.name] = achievement_class

        a, created = AchievementModel.objects.get_or_create(
            name=achievement_class.name,
            defaults={
                'title': achievement_class.title,
                'description': achievement_class.description,
            }
        )

        if not created:
            a.title = achievement_class.title
            a.description = achievement_class.description
            a.save()

        def check_achievement(instance, *args, **kwargs):
            model_instance = achievement_class.get_model_instance_for_observed_model(instance)
            check_and_give_achievement(achievement_class, model_instance)

        post_save.connect(
            check_achievement,
            sender=achievement_class.observed_model,
            weak=False,
            dispatch_uid='django_achievements.%s_save' % achievement_class.name
        )
        post_delete.connect(
            check_achievement,
            sender=achievement_class.observed_model,
            weak=False,
            dispatch_uid='django_achievements.%s_delete' % achievement_class.name
        )

        for model_instance in achievement_class.model.objects.all():
            check_and_give_achievement(achievement_class, model_instance)

        return achievement_class

    def unregister(self, name):
        import inspect
        if inspect.isclass(name) and issubclass(name, Achievement):
            name = name.name

        if name not in self._registry:
            raise NotRegistered

        achievement_class = self._registry.pop(name)

        try:
            AchievementModel.objects.get(name=achievement_class.name).delete()
        except:
            pass

        post_save.disconnect(
            sender=achievement_class.observed_model,
            dispatch_uid='django_achievements.%s_save' % achievement_class.name
        )
        post_delete.disconnect(
            sender=achievement_class.observed_model,
            dispatch_uid='django_achievements.%s_delete' % achievement_class.name
        )

    def unregister_all(self):
        for name in self._registry.keys():
            self.unregister(name)

AchievementRegistry = AchievementRegistry()
register = AchievementRegistry.register
unregister = AchievementRegistry.unregister
unregister_all_achievements = AchievementRegistry.unregister_all
