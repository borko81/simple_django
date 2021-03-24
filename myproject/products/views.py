from django.shortcuts import render, get_object_or_404

from .models import Product
from .forms import ProductForm


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


def product_new(request):
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        # Product.objects.create(title=title...)
    return render(request, 'product/new_product.html', context)
