import csv

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from accounts.mixins import AdminOrCompanyRequiredMixin
from accounts.utils import is_admin

from .forms import ProjectApplicationForm, ProjectForm
from .models import Project


def export_projects_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="projects.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nomi', 'Korxona', 'Kategoriya', 'Byudjet', 'Davomiyligi (oy)', 'Hudud', 'Holat', 'Yaratilgan vaqt'])
    for project in Project.objects.select_related('company'):
        writer.writerow([
            project.title,
            project.company.name,
            project.category,
            project.budget,
            project.duration_months,
            project.region,
            project.get_status_display(),
            project.created_at,
        ])
    return response


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        queryset = Project.objects.select_related('company')
        search = self.request.GET.get('search', '').strip()
        category = self.request.GET.get('category', '').strip()
        region = self.request.GET.get('region', '').strip()
        status = self.request.GET.get('status', '').strip()

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(company__name__icontains=search)
                | Q(description__icontains=search)
            )
        if category:
            queryset = queryset.filter(category=category)
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
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_region'] = self.request.GET.get('region', '')
        context['selected_status'] = self.request.GET.get('status', '')
        context['categories'] = Project.objects.order_by('category').values_list('category', flat=True).distinct()
        context['regions'] = Project.objects.order_by('region').values_list('region', flat=True).distinct()
        context['statuses'] = Project.Status.choices
        context['query_string'] = query_params.urlencode()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.select_related('company')


class ProjectCreateView(AdminOrCompanyRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        project = self.get_object()
        return (
            is_admin(self.request.user)
            or project.created_by_id == self.request.user.id
            or project.company.owner_id == self.request.user.id
        )

    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:list')

    def test_func(self):
        project = self.get_object()
        return (
            is_admin(self.request.user)
            or project.created_by_id == self.request.user.id
            or project.company.owner_id == self.request.user.id
        )


class ProjectApplicationCreateView(CreateView):
    form_class = ProjectApplicationForm
    template_name = 'projects/application_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project.objects.select_related('company'), pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.project = self.project
        messages.success(self.request, 'Hamkorlik arizangiz muvaffaqiyatli yuborildi.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def get_success_url(self):
        return reverse('projects:detail', kwargs={'pk': self.project.pk})
