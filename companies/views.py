import csv

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from accounts.mixins import AdminOrCompanyRequiredMixin
from accounts.utils import is_admin

from .forms import CompanyForm
from .models import Company


def export_companies_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="companies.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nomi', 'Hudud', 'Sanoat sohasi', 'Direktor', 'Telefon', 'Elektron pochta', 'Veb-sayt', 'Yaratilgan vaqt'])
    for company in Company.objects.all():
        writer.writerow([
            company.name,
            company.region,
            company.industry,
            company.director,
            company.phone,
            company.email,
            company.website,
            company.created_at,
        ])
    return response


class CompanyListView(ListView):
    model = Company
    template_name = 'companies/company_list.html'
    context_object_name = 'companies'
    paginate_by = 10

    def get_queryset(self):
        queryset = Company.objects.all()
        search = self.request.GET.get('search', '').strip()
        region = self.request.GET.get('region', '').strip()
        industry = self.request.GET.get('industry', '').strip()

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(region__icontains=search)
                | Q(industry__icontains=search)
                | Q(director__icontains=search)
            )
        if region:
            queryset = queryset.filter(region=region)
        if industry:
            queryset = queryset.filter(industry=industry)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_region'] = self.request.GET.get('region', '')
        context['selected_industry'] = self.request.GET.get('industry', '')
        context['regions'] = Company.objects.order_by('region').values_list('region', flat=True).distinct()
        context['industries'] = Company.objects.order_by('industry').values_list('industry', flat=True).distinct()
        context['query_string'] = query_params.urlencode()
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'


class CompanyCreateView(AdminOrCompanyRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/company_form.html'

    def form_valid(self, form):
        if not is_admin(self.request.user):
            form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('companies:detail', kwargs={'pk': self.object.pk})


class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/company_form.html'

    def test_func(self):
        company = self.get_object()
        return is_admin(self.request.user) or company.owner_id == self.request.user.id

    def get_success_url(self):
        return reverse_lazy('companies:detail', kwargs={'pk': self.object.pk})


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Company
    template_name = 'companies/company_confirm_delete.html'
    success_url = reverse_lazy('companies:list')

    def test_func(self):
        company = self.get_object()
        return is_admin(self.request.user) or company.owner_id == self.request.user.id
