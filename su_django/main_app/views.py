from django.shortcuts import render

def index(request):
    data = {
        'mdata': ["Downtown","Uptown","Midtown"],
    }
    return render(request, 'main_app/index.html', data)
