from django.shortcuts import render
from datetime import datetime


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Home view page</h1>")
    data = datetime.now()
    lookup = [
        "first item",
        "second item",
        "last item"
    ]
    return render(request, 'pages/home.html', {'user': request.user, 'data': data, "lookup": [x.upper() for x in lookup]})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact view page</h1>")
    email = '<h1>korea60@abv.bg</h1>'
    data = {
        'email': email
    }
    return render(request, 'pages/contact.html', data)


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About view page</h1>")
    return render(request, 'pages/about.html', {})
