from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title slug author publish status'.split()
    list_filter = 'status created publish author'.split()
    search_fields = 'title body'.split()
    prepopulated_fields = {'slug': ('title', )}
    # Id for user is number not name
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'