from django.urls import path

from .views import index, delid, edit

urlpatterns = [
    path('', index, name='home'),
    path('delid/<int:id>/', delid, name='delid'),
    path('edit/<int:id>/', edit, name='edit'),
]
