from django.apps import AppConfig

from config import config, uncached_config

class ConfigappConfig(AppConfig):
    name = 'config'
    verbose_name = "Database Configuration Storage"

    def ready(self):
        config._ready()
        uncached_config._ready()
