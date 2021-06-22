from django.urls import path
from .views import index, pet_all, pet_detail, pet_like, pets_create, pets_delete, pets_edit, pets_detail

app_name = 'common'
urlpatterns = [
    path('', index, name='index'),
    path('pets/', pet_all, name='pet_all'),
    path('pets/details/<int:pk>/', pet_detail, name='pet_detail'),
    path('pets/like/<int:pk>/', pet_like, name='pet_like'),

    path('pets/create/', pets_create, name='pets_create'),
    path('pets/edit/<int:pk>', pets_edit, name='pets_edit'),
    path('pets/delete/<int:pk>', pets_delete, name='pets_delete'),
    path('pets/detail/<int:pk>', pets_detail, name='pets_detail'),
]