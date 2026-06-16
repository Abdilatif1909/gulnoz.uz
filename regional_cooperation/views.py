from django.db.models import Count
from django.shortcuts import render

from companies.models import Company
from investments.models import Investment
from news.models import News
from projects.models import Project


def home(request):
    context = {
        'total_companies': Company.objects.count(),
        'total_projects': Project.objects.count(),
        'total_investments': Investment.objects.count(),
        'latest_projects': Project.objects.select_related('company')[:3],
        'latest_investments': Investment.objects.select_related('company')[:3],
        'latest_news': News.objects.filter(is_published=True)[:3],
        'regional_stats': Company.objects.values('region').annotate(
            companies_count=Count('id'),
            projects_count=Count('projects', distinct=True),
            investments_count=Count('investments', distinct=True),
        ).order_by('region')[:8],
    }
    return render(request, 'pages/home.html', context)
