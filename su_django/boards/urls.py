from django.urls import path
from .views import home, show_books

urlpatterns = [
    path('', home, name='home'),
    path('all/', show_books, name='all_book'),
]
