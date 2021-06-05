from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Todo


def index(request):
    todos = Todo.objects.all().order_by('is_done')
    context = {
        'todos': todos,
        'date': datetime.now()
    }
    return render(request, 'app/index.html', context)


def create_new(request):
    if request.method == 'POST':
        data = {}
        data['title'] = request.POST.get('title', None)
        data['description'] = request.POST.get('description', None)
        id_todo = request.POST.get('id', None)
        print(id_todo)
        if not id_todo:
            Todo.objects.create(title=data['title'], description=data['description'])
            return HttpResponse("Successfully added new todo")
        else:
            n = Todo.objects.get(id=id_todo)
            n.title = data['title']
            n.description = data['description']
            n.save()
            return HttpResponse("Successfully edit todo")
    return HttpResponse('Not allowed method')


def change_done(request):
    id = request.GET.get('id')
    dat = Todo.objects.get(id=id)
    dat.is_done = not dat.is_done
    dat.save()
    return HttpResponse('Change Done function')


def delete_todo(request):
    id = request.GET.get('id')
    data = get_object_or_404(Todo, id=id)
    name_data = data.title
    data.delete()
    return HttpResponse(f"Successfull delete todo {name_data}")


def edit_todo(request, id):

    todos = Todo.objects.all().order_by('is_done')
    context = {
        'todos': todos,
        'date': datetime.now()
    }
    data = get_object_or_404(Todo, id=id)
    context['title'] = data.title
    context['description'] = data.description
    context['id'] = data.id
    return render(request, 'app/index.html', context)
