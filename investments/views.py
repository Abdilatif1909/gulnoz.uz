import csv

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from accounts.mixins import AdminOrCompanyRequiredMixin, InvestorRequiredMixin
from accounts.utils import is_admin

from .forms import InvestmentForm, InvestorApplicationForm
from .models import Investment


def export_investments_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="investments.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nomi', 'Korxona', 'Sektor', 'Talab qilinadigan summa', 'Kutilayotgan ROI', 'Muddat (oy)', 'Hudud', 'Holat', 'Yaratilgan vaqt'])
    for investment in Investment.objects.select_related('company'):
        writer.writerow([
            investment.title,
            investment.company.name,
            investment.sector,
            investment.required_amount,
            investment.expected_roi,
            investment.investment_period_months,
            investment.region,
            investment.get_status_display(),
            investment.created_at,
        ])
    return response


class InvestmentListView(ListView):
    model = Investment
    template_name = 'investments/investment_list.html'
    context_object_name = 'investments'
    paginate_by = 10

    def get_queryset(self):
        queryset = Investment.objects.select_related('company')
        search = self.request.GET.get('search', '').strip()
        sector = self.request.GET.get('sector', '').strip()
        region = self.request.GET.get('region', '').strip()
        status = self.request.GET.get('status', '').strip()

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(company__name__icontains=search)
                | Q(description__icontains=search)
            )
        if sector:
            queryset = queryset.filter(sector=sector)
        if region:
            queryset = queryset.filter(region=region)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_sector'] = self.request.GET.get('sector', '')
        context['selected_region'] = self.request.GET.get('region', '')
        context['selected_status'] = self.request.GET.get('status', '')
        context['sectors'] = Investment.objects.order_by('sector').values_list('sector', flat=True).distinct()
        context['regions'] = Investment.objects.order_by('region').values_list('region', flat=True).distinct()
        context['statuses'] = Investment.Status.choices
        context['query_string'] = query_params.urlencode()
        return context


class InvestmentDetailView(DetailView):
    model = Investment
    template_name = 'investments/investment_detail.html'
    context_object_name = 'investment'

    def get_queryset(self):
        return Investment.objects.select_related('company')


class InvestmentCreateView(AdminOrCompanyRequiredMixin, CreateView):
    model = Investment
    form_class = InvestmentForm
    template_name = 'investments/investment_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('investments:detail', kwargs={'pk': self.object.pk})


class InvestmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Investment
    form_class = InvestmentForm
    template_name = 'investments/investment_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        investment = self.get_object()
        return is_admin(self.request.user) or investment.company.owner_id == self.request.user.id

    def get_success_url(self):
        return reverse_lazy('investments:detail', kwargs={'pk': self.object.pk})


class InvestmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Investment
    template_name = 'investments/investment_confirm_delete.html'
    success_url = reverse_lazy('investments:list')

    def test_func(self):
        investment = self.get_object()
        return is_admin(self.request.user) or investment.company.owner_id == self.request.user.id


class InvestorApplicationCreateView(InvestorRequiredMixin, CreateView):
    form_class = InvestorApplicationForm
    template_name = 'investments/investor_application_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.investment = get_object_or_404(Investment.objects.select_related('company'), pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.investment = self.investment
        messages.success(self.request, 'Investitsiya bo‘yicha qiziqish arizangiz muvaffaqiyatli yuborildi.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['investment'] = self.investment
        return context

    def get_success_url(self):
        return reverse('investments:detail', kwargs={'pk': self.investment.pk})
