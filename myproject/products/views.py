from django.shortcuts import render, get_object_or_404

from .models import Product
from .forms import ProductForm, RawProductForm


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price
    }
    return render(request, 'product/detail.html', context)


# def product_new(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'product/new_product.html', context)


# def product_new(request):
#     """ Raw Django forms """
#     context = {}
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         # Product.objects.create(title=title...)
#     return render(request, 'product/new_product.html', context)


def product_new(request):
    """ Pure django forms """
    pure_form = RawProductForm()
    if request.method == 'POST':
        pure_form = RawProductForm(request.POST)
        if pure_form.is_valid():
            Product.objects.create(**pure_form.cleaned_data)
            pure_form = RawProductForm()
    context = {'form': pure_form}
    return render(request, 'product/new_product.html', context)
