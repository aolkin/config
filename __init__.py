

from . import models

class _Config:
    def __init__(self, caching=True):
        super().__setattr__("_use_cache",caching)

    def __getattr__(self,key):
        return models.Config.get(key,nocache=not self._use_cache)
    __getitem__ = __getattr__

    def __setattr__(self,key,value):
        return models.Config.set(key,value)
    __setitem__ = __setattr__

    def get(self,key,fallback=None):
        return models.Config.get(key,fallback,nocache=not self._use_cache)

    def clear_cache(self):
        models.clear_cache()

    @property
    def use_cache(self):
        return self._use_cache

    @use_cache.setter
    def use_cache(self, val):
        self._use_cache = val

config = _Config()
uncached_config = _Config(False)
