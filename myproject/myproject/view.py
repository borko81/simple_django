from django.shortcuts import render
from django.http import HttpResponse


show_page_info = {
    1: 'First page',
    2: 'Second page',
}


def hello(request):
    text = "<h1>Inside black power</h1>"
    return HttpResponse(text)


def from_num(request, number):
    page_text = show_page_info.get(number, 'Not found this number')
    text = "<h1>The page is {}</h1>".format(page_text)
    return HttpResponse(text)


def load_shano_page(request):
    return render(request, 'check.html', {})
