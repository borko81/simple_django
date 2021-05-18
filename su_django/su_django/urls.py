from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('cityes.urls')),
    path('main/', include('main_app.urls')),
    path('secondary/', include('secondary_app.urls')),
]
