from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    hello_world
)

app_name = 'portfolio'
urlpatterns = [
    path('', hello_world, name='hello'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

