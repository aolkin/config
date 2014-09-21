
from . import config, uncached_config

def configuration(request):
    return {"options": config, "uncached_options": uncached_config}
