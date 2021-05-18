from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'town', 'age')
    list_filter = ('name', 'town')

    class Meta:
        ordering = ('name', )