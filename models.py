from django.db import models
from django.db.utils import Error
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

_cache = {}

class Config(models.Model):
    key = models.CharField(max_length=40,primary_key=True,unique=True)
    value = models.CharField(max_length=240,blank=True)
    missing = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<{}: {}>".format(self.key,self.value)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Configuration Datum"
        verbose_name_plural = "Configuration Data"
    
    @classmethod
    def get(self,key,fallback=None,nocache=False):
        try:
            if nocache:
                raise KeyError("Do not cache")
            res = _cache[key]
        except KeyError:
            try:
                obj = self.objects.get(key=key)
                if obj.missing:
                    return fallback
                res = obj.value
                _cache[key] = res
            except self.DoesNotExist as err:
                self.objects.create(key=key,value=fallback or "",missing=True)
                return fallback
            except Error as err:
                print(repr(err))
                return fallback
        return res

    @classmethod
    def set(self,key,val):
        obj, created = self.objects.get_or_create(key=key)
        obj.missing = False
        obj.value = val
        obj.save()

@receiver(post_save, sender=Config)
def update_cache(sender, instance, **kwargs):
    _cache[instance.key] = instance.value
        
def clear_cache():
    _cache.clear()
