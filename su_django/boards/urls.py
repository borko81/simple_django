from django.urls import path
from .views import home, show_books, upload_book, edit_book, delete_book

urlpatterns = [
    path('', home, name='home'),
    path('all/', show_books, name='all_book'),
    path('new/', upload_book, name='upload_book'),
    path('edit/<int:book_id>/book/',edit_book, name='edit_book'),
    path('delete/<int:book_id>/book', delete_book, name='delete_book'),
]
