from django.shortcuts import render

def index(request):
    return render(request, 'secondary_app/index.html')
