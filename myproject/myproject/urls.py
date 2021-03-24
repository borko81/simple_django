from django.contrib import admin
from django.urls import path
from .view import from_num, hello, load_shano_page

from pages import views as pages
from products import views as product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('begin', hello, name='hello'),
    path('num_page/<int:number>/', from_num, name='from_num'),
    path('shano/', load_shano_page, name='shano'),

    path('home/', pages.home_view, name='home_view'),
    path('contact/', pages.contact_view, name='contact_view'),
    path('about/', pages.about_view, name='about_view'),

    path('product/detail/<int:id>/', product.product_detail_view, name='detail_product'),
    path('product/new/', product.product_new, name='product_new'),
]
