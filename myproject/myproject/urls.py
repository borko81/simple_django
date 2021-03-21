from django.contrib import admin
from django.urls import path
from .view import from_num, hello, load_shano_page

from pages import views as pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('begin', hello, name='hello'),
    path('num_page/<int:number>/', from_num, name='from_num'),
    path('shano/', load_shano_page, name='shano'),

    path('home_view/', pages.home_view, name='home_view'),
    path('contact_view', pages.contact_view, name='contact_view'),
    path('about_view', pages.contact_view, name='about_view'),
]
