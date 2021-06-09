from django.core.serializers import serialize
from django.shortcuts import render

from .models import Person


def index(request):
    result = {}
    data = Person.objects.all()
    result = serialize('json', data)
    return render(request, 'cities/index.html', {'data': data})
