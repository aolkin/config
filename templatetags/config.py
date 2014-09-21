from django import template

register = template.Library()

from ..models import Config

def get_opt(key,fallback=None):
    return Config.get(key,fallback)

register.simple_tag(get_opt)
register.simple_tag(get_opt,name="option")

def get_nocache(key,fallback=None):
    return Config.get(key,fallback, nocache=True)

register.simple_tag(get_nocache)
register.simple_tag(get_nocache,name="option_uncached")
