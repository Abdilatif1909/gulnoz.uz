from django import forms

from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'slug',
            'short_description',
            'content',
            'image',
            'author',
            'is_published',
        ]
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 3}),
            'content': forms.Textarea(attrs={'rows': 8}),
        }
        labels = {
            'title': 'Sarlavha',
            'slug': 'Slug',
            'short_description': 'Qisqa tavsif',
            'content': 'Matn',
            'image': 'Rasm',
            'author': 'Muallif',
            'is_published': 'Nashr etilgan',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False
        self.fields['slug'].help_text = 'Bo‘sh qoldirilsa, sarlavhadan avtomatik yaratiladi.'
        for field_name, field in self.fields.items():
            if field_name == 'is_published':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
