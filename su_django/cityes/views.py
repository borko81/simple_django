from django.shortcuts import render

from .models import Person


def index(request):
    content = {
        'data': Person.objects.all()
    }
    return render(request, 'base.html', content)