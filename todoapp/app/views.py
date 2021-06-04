from django.shortcuts import render

from datetime import datetime

from .models import Todo



def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'date': datetime.now()
    }
    return render(request, 'app/index.html', context)
