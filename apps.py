from django.apps import AppConfig
from django.conf import settings

from config import *

class ConfigappConfig(AppConfig):
    name = 'config'
    verbose_name = (settings.CONFIGURATION_APP_TITLE if
                    hasattr(settings, "CONFIGURATION_APP_TITLE") else
                    "Database Configuration Storage")

    def ready(self):
        config._ready()
        uncached_config._ready()
        numeric_config._ready()
