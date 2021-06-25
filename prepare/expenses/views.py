from django.shortcuts import render, redirect

from expenses.forms import ProfileForm
from expenses.models import Profile, Expense


def home_page(request):

    try:
        p = Profile.objects.all()[0]
        expenses = Expense.objects.all()
        return render(request, 'home-with-profile.html', {'expenses': expenses, 'total': p.budget, 'left': p.budget - sum(e.price for e in expenses)})
    except:
        form = ProfileForm()
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')
        return render(request, 'home-no-profile.html', {'form': form})


def create(request):

    if request.method == 'POST':
        title = request.POST['title']
        image_url = request.POST['image_url']
        description = request.POST['description']
        price = request.POST['price']
        Expense.objects.create(title=title, image_url=image_url, description=description, price=price)
        return redirect('home_page')
    return render(request, 'expense-create.html', )


def edit(request, pk):
    e = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'expense-edit.html', {'title': e.title, 'description': e.description, 'image_url': e.image_url, 'price': e.price, 'pk': e.id})
    e.title = request.POST['title']
    e.description = request.POST['description']
    e.image_url = request.POST['image_url']
    e.price = request.POST['price']
    e.save()
    return redirect('home_page')


def delete(request, pk):
    e = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'expense-delete.html',
                      {'title': e.title, 'description': e.description, 'image_url': e.image_url, 'price': e.price,
                       'pk': e.id})
    e.delete()
    return redirect('home_page')


def profile(request):
    p = Profile.objects.all()[0]
    expenses = Expense.objects.all()
    return render(request, 'profile.html', {'profile': p, 'left': p.budget - sum(e.price for e in expenses)})


def profile_edit(request):
    p = Profile.objects.all()[0]
    if request.method == 'GET':
        return render(request, 'profile-edit.html', {'budget': p.budget, 'first_name': p.first_name, 'last_name': p.last_name})
    p.budget = request.POST['budget']
    p.first_name = request.POST['first_name']
    p.last_name = request.POST['last_name']
    p.save()
    return redirect('home_page')


def profile_delete(request):
    p = Profile.objects.get(pk=1)
    p.delete()
    return redirect('home_page')
