from django.urls import path

from .views import index, delid

urlpatterns = [
    path('', index, name='home'),
    path('delid/<int:id>/', delid, name='delid'),
]
