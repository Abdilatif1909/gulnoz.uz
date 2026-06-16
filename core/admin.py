from django.contrib import admin

from .models import ActivityLog, ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
    search_fields = ('full_name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'user', 'description', 'created_at')
    search_fields = ('description', 'user__username')
    list_filter = ('action', 'created_at')
    readonly_fields = ('user', 'action', 'description', 'created_at')
    ordering = ('-created_at',)
