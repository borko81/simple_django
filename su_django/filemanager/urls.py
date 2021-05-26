from django.urls import path
from .views import (
    show_files
)

urlpatterns = [
    path('', show_files, name='show_files'),
]