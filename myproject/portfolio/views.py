from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Project

# Create your views here.
def hello_world(request):
    project = Project.objects.all()
    context = {
        'project': project
    }
    return render(request, 'portfolio/index.html', context)