
from . import *

def configuration(request):
    return {
        "options": config,
        "uncached_options": uncached_config,
        "numeric_options": numeric_config,
    }
