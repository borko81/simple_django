from django.shortcuts import render

from .models import Board, Book


def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/index.html', {'boards': boards})


def show_books(request):
    shelf = Book.objects.all()
    content = {
        'shelf': shelf
    }
    return render(request, 'boards/all_books.html', content)
