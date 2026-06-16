from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
