from .models import AchievementModel


def check_and_give_achievement(achievement_class, model_instance):
    try:
        achievement_object = AchievementModel.objects.get(name=achievement_class.name)
    except:
        raise "Unknown achievement name: %s" % achievement_class.name

    achievable = achievement_class.get_achievable(model_instance)
    check_res = achievement_class.check_for(model_instance)
    print 'checking ' + str(achievement_object) + ' ' + str(model_instance)
    if check_res and achievement_object not in achievable.achievements.all():
        print 'adding ' + str(achievement_object) + ' ' + str(model_instance)
        achievable.achievements.add(achievement_object)
    if not check_res and achievement_object in achievable.achievements.all():
        print 'removing ' + str(achievement_object) + ' ' + str(model_instance)
        achievable.achievements.remove(achievement_object)
