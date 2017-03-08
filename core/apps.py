from __future__ import unicode_literals

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from django.db.backends.signals import connection_created
        from django.dispatch import receiver

        @receiver(connection_created)
        def register_achievements(*args, **kwargs):
            import achievements
