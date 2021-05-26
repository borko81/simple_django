import os
from os import startfile

from django.http import HttpResponse
from django.shortcuts import render

from .forms import AskForm


def return_only_name_of_file(filename):
    return "".join(filename.split('.')[:-1])


class Directory:

    def __init__(self, path):
        self.path = path

    def search_it(self, pattern):
        result = {}
        for root, dirname, filename in os.walk(self.path):
            for file in filename:
                if file.endswith(pattern):
                    result[return_only_name_of_file(file)] = os.path.join(root, file)
        return result


def show_files(requests):
    ask = requests.POST.get('name')
    ask = '.' + ask
    files = Directory(r'D:\movies')
    content = {
        'files': files.search_it(ask)
    }
    return render(requests, 'filemanager/index.html', content)


def open_path(request, path):
    startfile(path)
    return HttpResponse('Now playing {}'.format(path))


def ask_and_return_from_form(request):
    forms = AskForm()
    content = {
        'forms': forms
    }
    return render(request, 'filemanager/form_ask.html', content)