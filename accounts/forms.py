from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = 'Foydalanuvchi nomi'
        self.fields['password'].label = 'Parol'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Elektron pochta', required=True)
    role = forms.ChoiceField(
        label='Rol',
        choices=[
            (UserProfile.Role.COMPANY, 'Korxona'),
            (UserProfile.Role.INVESTOR, 'Investor'),
        ]
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Foydalanuvchi nomi'
        self.fields['password1'].label = 'Parol'
        self.fields['password2'].label = 'Parolni tasdiqlash'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-select' if isinstance(field.widget, forms.Select) else 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.profile.role = self.cleaned_data['role']
            user.profile.save()
        return user
