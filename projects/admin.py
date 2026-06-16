from django.contrib import admin

from .models import Project, ProjectApplication


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'category', 'region', 'budget', 'duration_months', 'status', 'created_at')
    search_fields = ('title', 'company__name', 'region')
    list_filter = ('category', 'status')
    autocomplete_fields = ('company',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(ProjectApplication)
class ProjectApplicationAdmin(admin.ModelAdmin):
    list_display = ('project', 'applicant_company_name', 'contact_person', 'phone', 'email', 'created_at')
    search_fields = ('project__title', 'applicant_company_name', 'contact_person', 'email')
    list_filter = ('created_at',)
    autocomplete_fields = ('project',)
    readonly_fields = ('created_at',)
