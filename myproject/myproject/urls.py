from django.contrib import admin
from django.urls import path
from .view import from_num, hello, load_shano_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('begin', hello, name='hello'),
    path('num_page/<int:number>/', from_num, name='from_num'),
    path('shano/', load_shano_page, name='shano')
]
