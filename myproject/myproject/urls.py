from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from pages import views as pages


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

    path('port/', include('portfolio.urls')),

    path('book/', include('bookblog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
