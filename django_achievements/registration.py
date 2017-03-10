from .registry import AchievementRegistry


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
        """
        :type instance: model
        """
        raise NotImplementedError

    @classmethod
    def get_achievable(cls, instance):
        """
        :type instance: model
        :return achievable - model with m2m field 'achievements'
        """
        raise NotImplementedError

    @classmethod
    def get_model_instance_for_observed_model(cls, instance):
        """
        :type instance: observed_model
        """
        if cls.observed_model is None:
            return instance
        else:
            raise NotImplementedError

    @classmethod
    def get_observed_model(cls):
        if cls.observed_model is None:
            return cls.model
        else:
            return cls.observed_model


AchievementRegistry = AchievementRegistry()
register = AchievementRegistry.register
unregister = AchievementRegistry.unregister
unregister_all_achievements = AchievementRegistry.unregister_all
