from celery import shared_task

from django_achievements.utils import check_and_give_achievement


@shared_task
def check_achievement_task(achievement_class_name, model_instance_id):
    from django_achievements.registration import AchievementRegistry
    achievement_class = AchievementRegistry._registry[achievement_class_name]
    model_instance = achievement_class.model.objects.get(id=model_instance_id)
    check_and_give_achievement(achievement_class, model_instance)
