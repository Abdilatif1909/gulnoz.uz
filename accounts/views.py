from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import BootstrapAuthenticationForm, RegistrationForm


class UserLoginView(LoginView):
    authentication_form = BootstrapAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard:index')

    def form_valid(self, form):
        messages.success(self.request, 'Tizimga muvaffaqiyatli kirdingiz.')
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    http_method_names = ['get', 'post', 'options']

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Tizimdan muvaffaqiyatli chiqdingiz.')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi.')
        return response
