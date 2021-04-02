from django import forms
from django.db.models.query import prefetch_related_objects
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm

# Create your views here.


def hello_world(request):
    project = Project.objects.all()
    form = ProjectForm()

    if request.method == 'POST':

        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProjectForm()
            return redirect('portfolio:hello')
    else:
        context = {
            'project': project,
            'form': form
        }
        return render(request, 'portfolio/index.html', context)
