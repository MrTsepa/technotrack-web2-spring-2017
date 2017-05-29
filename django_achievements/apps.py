from __future__ import unicode_literals

from django.apps import AppConfig


class DjangoAchievementsConfig(AppConfig):
    name = 'django_achievements'

    def ready(self):
        from application import settings
        if not settings.TESTING:
            from django.db.backends.signals import connection_created

            def register_achievements(*args, **kwargs):
                try:
                    from django.utils.module_loading import autodiscover_modules
                    autodiscover_modules('achievements')
                except Exception as e:
                    print e
                    print "Maybe, you need to run migrations first"

            connection_created.connect(register_achievements, weak=False)
