import json

from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render

from companies.models import Company
from investments.models import Investment, InvestorApplication
from projects.models import Project, ProjectApplication
from core.models import ActivityLog


def _chart_payload(queryset, label_field, value_field='total'):
    rows = list(queryset)
    return {
        'labels': [row[label_field] for row in rows],
        'values': [row[value_field] for row in rows],
    }


def dashboard(request):
    companies_by_region = Company.objects.values('region').annotate(total=Count('id')).order_by('region')
    projects_by_category = Project.objects.values('category').annotate(total=Count('id')).order_by('category')
    investments_by_sector = Investment.objects.values('sector').annotate(total=Count('id')).order_by('sector')
    project_statuses = Project.objects.values('status').annotate(total=Count('id')).order_by('status')
    investment_statuses = Investment.objects.values('status').annotate(total=Count('id')).order_by('status')
    monthly_growth = Project.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(total=Count('id')).order_by('month')

    project_status_labels = dict(Project.Status.choices)
    investment_status_labels = dict(Investment.Status.choices)

    project_status_payload = {
        'labels': [project_status_labels[row['status']] for row in project_statuses],
        'values': [row['total'] for row in project_statuses],
    }
    investment_status_payload = {
        'labels': [investment_status_labels[row['status']] for row in investment_statuses],
        'values': [row['total'] for row in investment_statuses],
    }

    context = {
        'total_companies': Company.objects.count(),
        'total_projects': Project.objects.count(),
        'total_investments': Investment.objects.count(),
        'total_partnership_applications': ProjectApplication.objects.count(),
        'total_investor_applications': InvestorApplication.objects.count(),
        'companies_by_region_json': json.dumps(_chart_payload(companies_by_region, 'region')),
        'projects_by_category_json': json.dumps(_chart_payload(projects_by_category, 'category')),
        'investments_by_sector_json': json.dumps(_chart_payload(investments_by_sector, 'sector')),
        'project_status_json': json.dumps(project_status_payload),
        'investment_status_json': json.dumps(investment_status_payload),
        'recent_activities': ActivityLog.objects.select_related('user')[:8],
        'top_regions': Company.objects.values('region').annotate(total=Count('id')).order_by('-total', 'region')[:5],
        'top_industries': Company.objects.values('industry').annotate(total=Count('id')).order_by('-total', 'industry')[:5],
        'monthly_growth': monthly_growth,
    }
    return render(request, 'dashboard/dashboard.html', context)
