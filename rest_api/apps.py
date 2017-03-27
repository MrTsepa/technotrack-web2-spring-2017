from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class RestApiConfig(AppConfig):
    name = 'rest_api'

    def ready(self):
        autodiscover_modules('api')
