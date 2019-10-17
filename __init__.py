
from importlib import import_module

default_app_config = "config.apps.ConfigappConfig"

class _Config:
    def __init__(self, caching=True, numeric=False):
        self._use_cache = caching
        self._numeric = numeric

    def _ready(self):
        self.__models = import_module("config.models")
        
    def __getattr__(self, key):
        if key.startswith("_"):
            return super().__getattribute__(key)
        return self.get(key)
    __getitem__ = __getattr__

    def __setattr__(self, key, value):
        if key.startswith("_"):
            return super().__setattr__(key, value)
        return self.__models.Config.set(key,value)
    __setitem__ = __setattr__

    def get(self, key, fallback=None, skip_numeric=False):
        if self._numeric and not skip_numeric:
            try:
                return int(self.get(key, fallback, True))
            except ValueError:
                try:
                    return float(self.get(key, fallback, True))
                except:
                    pass
        return self.__models.Config.get(key, fallback,
                                        nocache=not self._use_cache)

    def get_int(self, key, fallback=None):
        return int(self.get_float(key, fallback))
    
    def get_float(self, key, fallback=None):
        try:
            return float(self.get(key,fallback))
        except ValueError as err:
            return fallback

    def clear_cache(self):
        self.__models.clear_cache()

    @property
    def use_cache(self):
        return self._use_cache

    @use_cache.setter
    def use_cache(self, val):
        self._use_cache = val

config = _Config()
uncached_config = _Config(False)
numeric_config = _Config(True, True)

__all__ = ["config", "uncached_config", "numeric_config"]
