from django.urls import path

from .views import index, edit, create

app_name = 'books'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('edit/<int:id>/', edit, name='edit'),
]