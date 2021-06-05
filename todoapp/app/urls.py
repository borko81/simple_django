from django.urls import path

from .views import index, create_new, change_done, delete_todo, edit_todo

urlpatterns = [
    path('', index, name='index'),
    path('create_new/', create_new, name='create_new'),
    path('change_done/', change_done, name='change_done'),
    path('delete/', delete_todo, name='delete_todo'),
    path('edit/<int:id>/', edit_todo, name='edit_todo'),
]
