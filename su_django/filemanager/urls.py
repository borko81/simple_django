from django.urls import path
from .views import (
    show_files,
    open_path,
    ask_and_return_from_form,
)

urlpatterns = [
    path('', ask_and_return_from_form, name='ask_for_what'),
    path('show_all/', show_files, name='show_all'),
    path('open/<str:path>/', open_path, name='open_path'),
]