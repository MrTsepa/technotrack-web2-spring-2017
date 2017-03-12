from django.db.models.signals import post_save, post_delete

from .models import AchievementModel
from .utils import check_and_give_achievement


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
            if not isinstance(model_instance, achievement_class.model):
                return
            check_and_give_achievement(achievement_class, model_instance)

        post_save.connect(
            check_achievement,
            sender=achievement_class.get_observed_model(),
            weak=False,
            dispatch_uid='django_achievements.%s_save' % achievement_class.name
        )
        post_delete.connect(
            check_achievement,
            sender=achievement_class.get_observed_model(),
            weak=False,
            dispatch_uid='django_achievements.%s_delete' % achievement_class.name
        )

        for model_instance in achievement_class.model.objects.all():
            check_and_give_achievement(achievement_class, model_instance)

        return achievement_class

    def unregister(self, name):
        import inspect
        from registration import Achievement
        if inspect.isclass(name) and issubclass(name, Achievement):
            name = name.name

        if name not in self._registry:
            raise NotRegistered

        achievement_class = self._registry.pop(name)
        assert issubclass(achievement_class, Achievement)

        try:
            AchievementModel.objects.get(name=achievement_class.name).delete()
        except:
            pass

        post_save.disconnect(
            sender=achievement_class.get_observed_model(),
            dispatch_uid='django_achievements.%s_save' % achievement_class.name
        )
        post_delete.disconnect(
            sender=achievement_class.get_observed_model(),
            dispatch_uid='django_achievements.%s_delete' % achievement_class.name
        )

    def unregister_all(self):
        for name in self._registry.keys():
            self.unregister(name)
