from django.apps import AppConfig

from config import config

class ConfigappConfig(AppConfig):
    name = 'Database Config App'

    def ready(self):
        print("Readying configuration app...")
        config._ready()
