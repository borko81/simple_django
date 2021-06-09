from django.core.serializers import serialize
from django.http import JsonResponse

from .models import Person


def index(request):
    result = {}
    data = Person.objects.all()
    result = serialize('json', data)
    return JsonResponse(result, safe=False)
