import os

from django.shortcuts import render


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
    files = Directory(r'D:\movies')
    content = {
        'files': files.search_it(('.avi', '.mkv'))
    }
    return render(requests, 'filemanager/index.html', content)
