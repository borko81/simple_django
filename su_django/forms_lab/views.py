from django.shortcuts import render, redirect

from .forms import MyForm
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo_app/index.html', {'todos': todos})


def create(request):
    forms = MyForm(request.POST or None)
    contex = {
        'todo': forms
    }
    if request.method == 'POST':
        if forms.is_valid():
            result = {}
            result['name'] = forms.cleaned_data['name']
            result['age'] = forms.cleaned_data['age']
            result['email'] = forms.cleaned_data['email']
            result['password'] = forms.cleaned_data['password']
            result['text'] = forms.cleaned_data['text']
            Todo.objects.create(**result)
            return redirect('index')
    return render(request, 'todo_app/create.html', contex)
