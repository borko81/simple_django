from django.contrib import admin

from .models import BookUserModel, BookModel


@admin.register(BookUserModel)
class BookUserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    pass
