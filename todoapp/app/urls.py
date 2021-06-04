from django.urls import path

from .views import index, create_new, change_done


urlpatterns = [
    path('', index, name='index'),
    path('create_new/', create_new, name='create_new'),
    path('change_done/', change_done, name='change_done'),
]