from django import forms

from accounts.utils import is_admin, is_company
from companies.models import Company

from .models import Investment, InvestorApplication


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = [
            'title',
            'company',
            'sector',
            'required_amount',
            'expected_roi',
            'investment_period_months',
            'region',
            'description',
            'benefits',
            'risks',
            'status',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'benefits': forms.Textarea(attrs={'rows': 5}),
            'risks': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Investitsiya nomi',
            'company': 'Korxona',
            'sector': 'Sektor',
            'required_amount': 'Talab qilinadigan summa',
            'expected_roi': 'Kutilayotgan ROI',
            'investment_period_months': 'Investitsiya muddati (oy)',
            'region': 'Hudud',
            'description': 'Tavsif',
            'benefits': 'Afzalliklar',
            'risks': 'Xatarlar',
            'status': 'Holat',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and is_company(user):
            self.fields['company'].queryset = Company.objects.filter(owner=user)
        elif user and is_admin(user):
            self.fields['company'].queryset = Company.objects.all()
        else:
            self.fields['company'].queryset = Company.objects.none()
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-select' if isinstance(field.widget, forms.Select) else 'form-control'


class InvestorApplicationForm(forms.ModelForm):
    class Meta:
        model = InvestorApplication
        fields = [
            'investor_name',
            'organization',
            'phone',
            'email',
            'investment_amount',
            'message',
        ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'investor_name': 'Investor ismi',
            'organization': 'Tashkilot',
            'phone': 'Telefon',
            'email': 'Elektron pochta',
            'investment_amount': 'Investitsiya summasi',
            'message': 'Xabar',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
