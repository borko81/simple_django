from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Home view page</h1>")
    return render(request, 'pages/home.html', {'user': request.user})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact view page</h1>")
    return render(request, 'pages/contact.html', {})


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About view page</h1>")
    return render(request, 'pages/about.html', {})
