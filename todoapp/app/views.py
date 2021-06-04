from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'date': datetime.now()
    }
    return render(request, 'app/index.html', context)


def create_new(request):
    if request.method == 'POST':
        print('-' * 100)
        print(request)
        print('-' * 100)
        data = {}
        data['title'] = request.POST.get('title', None)
        data['description'] = request.POST.get('description', None)
        Todo.objects.create(title=data['title'], description=data['description'])
        return HttpResponse("Successfully added new todo")
    return HttpResponse('Not allowed method')


def change_done(request):
    id = request.GET.get('id')
    dat = Todo.objects.get(id=id)
    dat.is_done = not dat.is_done
    dat.save()
    return HttpResponse('Change Done function')
