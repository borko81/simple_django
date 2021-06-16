from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookModelForm
from .models import BookModel


def index(request):
    all_books = BookModel.objects.all()
    return render(request, 'index.html', {'books': all_books})


def create(request):
    context = {}
    form = BookModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('books:index')

    context['form'] = form
    return render(request, 'create.html', context)


def edit(request, id):
    context = {}
    obj = get_object_or_404(BookModel, id=id)
    form = BookModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        q = form.save(commit=False)
        q.save()
        messages.success(request, 'Success!')
        return redirect('books:index')

    context['form'] = form
    return render(request, 'edit.html', context)
