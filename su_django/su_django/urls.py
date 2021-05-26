from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('cityes.urls')),
    path('main/', include('main_app.urls')),
    path('secondary/', include('secondary_app.urls')),
    path('boards/', include('boards.urls')),

    path('files/', include('filemanager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
