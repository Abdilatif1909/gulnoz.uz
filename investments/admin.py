from django.contrib import admin

from .models import Investment, InvestorApplication


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'sector',
        'region',
        'required_amount',
        'expected_roi',
        'investment_period_months',
        'status',
        'created_at',
    )
    search_fields = ('title', 'company__name', 'sector', 'region')
    list_filter = ('sector', 'region', 'status')
    readonly_fields = ('created_at',)
    autocomplete_fields = ('company',)
    ordering = ('-created_at',)


@admin.register(InvestorApplication)
class InvestorApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'investment',
        'investor_name',
        'organization',
        'phone',
        'email',
        'investment_amount',
        'created_at',
    )
    search_fields = ('investment__title', 'investor_name', 'organization', 'email')
    list_filter = ('created_at', 'investment__sector')
    readonly_fields = ('created_at',)
    autocomplete_fields = ('investment',)
