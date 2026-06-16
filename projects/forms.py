from django import forms

from accounts.utils import is_admin, is_company
from companies.models import Company

from .models import Project, ProjectApplication


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'company',
            'category',
            'budget',
            'duration_months',
            'region',
            'description',
            'requirements',
            'status',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'requirements': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Loyiha nomi',
            'company': 'Korxona',
            'category': 'Kategoriya',
            'budget': 'Byudjet',
            'duration_months': 'Davomiyligi (oy)',
            'region': 'Hudud',
            'description': 'Tavsif',
            'requirements': 'Talablar',
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


class ProjectApplicationForm(forms.ModelForm):
    class Meta:
        model = ProjectApplication
        fields = [
            'applicant_company_name',
            'contact_person',
            'phone',
            'email',
            'message',
        ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'applicant_company_name': 'Arizachi korxona nomi',
            'contact_person': 'Mas’ul shaxs',
            'phone': 'Telefon',
            'email': 'Elektron pochta',
            'message': 'Xabar',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
