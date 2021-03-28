from django.contrib import admin
from django.urls import path, include

from pages import views as pages
from blog import views as blog

from .view import from_num, hello, load_shano_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('begin', hello, name='hello'),
    path('num_page/<int:number>/', from_num, name='from_num'),
    path('shano/', load_shano_page, name='shano'),

    path('home/', pages.home_view, name='home_view'),
    path('contact/', pages.contact_view, name='contact_view'),
    path('about/', pages.about_view, name='about_view'),

    path('product/', include('products.urls')),
    path('blog/', include('blog.urls')),
]
