
from .models import Autocomplete

from django.http import JsonResponse

def autocomplete_json(request):
    qs = Autocomplete.objects.filter(
        key=request.GET["key"],
        value__icontains=request.GET.get("q", ""))
    return JsonResponse(list(
        [i for l in qs.distinct().values_list("value") for i in l]),
                        safe=False)
