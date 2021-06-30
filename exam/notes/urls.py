from django.urls import path
from .views import (
    home_page,
    add,
    edit,
    delete,
    details,
    profile,
    delete_profile
)

urlpatterns = [
    path('', home_page, name='home_page'),
    path('add/', add, name='add_note'),
    path('edit/<int:id>/', edit, name='edit_note'),
    path('delete/<int:id>/', delete, name='delete_note'),
    path('details/<int:id>/', details, name='details_note'),
    path('profile/', profile, name='profile'),
    path('delete_profile/<int:id>/', delete_profile, name='delete_profile'),
]

