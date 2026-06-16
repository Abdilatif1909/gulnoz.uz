from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'region', 'industry', 'director', 'phone', 'email', 'created_at')
    search_fields = ('name', 'region', 'industry')
    list_filter = ('region', 'industry')
    autocomplete_fields = ('owner',)
    readonly_fields = ('created_at',)
    ordering = ('name',)
