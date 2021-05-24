from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import BookCreate
from .models import Board, Book


def home(request):
    boards = Board.objects.all()
    print("-"*20, '\n', request)
    messages.success(request, 'Success messages')
    return render(request, 'boards/index.html', {'boards': boards})


def show_books(request):
    shelf = Book.objects.all()
    content = {
        'shelf': shelf
    }
    return render(request, 'boards/all_books.html', content)


def upload_book(request):
    forms = BookCreate()
    if request.method == 'POST':
        forms = BookCreate(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'New book added successfully')
            return redirect('all_book')
        else:
            return HttpResponse('Not valid form reload in <a href={{ url: "index" }}>reload</a>')
    return render(request, 'boards/new_book.html', {'forms': forms})


def edit_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('all_book')
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('all_book')
    return render(request, 'boards/new_book.html', {'forms': book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('all_book')
    book_sel.delete()
    messages.success(request, f'Book with id {book_id} delete successfully')
    return redirect('all_book')

