from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'region',
            'industry',
            'director',
            'phone',
            'email',
            'website',
            'description',
            'logo',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'name': 'Korxona nomi',
            'region': 'Hudud',
            'industry': 'Sanoat sohasi',
            'director': 'Direktor',
            'phone': 'Telefon',
            'email': 'Elektron pochta',
            'website': 'Veb-sayt',
            'description': 'Tavsif',
            'logo': 'Logotip',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            css_class = 'form-control'
            if field_name == 'logo':
                css_class = 'form-control'
            field.widget.attrs['class'] = css_class
