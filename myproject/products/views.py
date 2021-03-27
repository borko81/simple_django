from django.shortcuts import redirect, render, get_object_or_404

from .models import Product
from .forms import ProductForm


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def product_detail_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price
    }
    return render(request, 'product/detail.html', context)


def product_new(request):
    """ Pure django forms, redirect after success """
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        return redirect(product_new)

    context = {
        'form': form
    }
    return render(request, 'product/new_product.html', context)


# def product_new(request):
#     """ Raw Django forms """
#     context = {}
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         # Product.objects.create(title=title...)
#     return render(request, 'product/new_product.html', context)


# def product_new(request):
#     """ Pure django forms """
#     pure_form = RawProductForm()
#     if request.method == 'POST':
#         pure_form = RawProductForm(request.POST)
#         if pure_form.is_valid():
#             Product.objects.create(**pure_form.cleaned_data)
#             pure_form = RawProductForm()
#     context = {'form': pure_form}
#     return render(request, 'product/new_product.html', context)

def edit_product(request, product_id):
    obj = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(view_all_product)
    content = {
        'form': form
    }
    return render(request, 'product/edit_product.html', content)


def view_all_product(request):
    """ Show all product's """
    obj = Product.objects.all()
    content = {
        'all': obj
    }
    return render(request, 'product/all_product.html', content)