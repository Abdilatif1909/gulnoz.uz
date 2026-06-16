from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from accounts.utils import get_user_role
from accounts.utils import is_admin
from companies.models import Company
from investments.models import Investment, InvestorApplication
from news.models import News
from projects.models import Project, ProjectApplication

from .forms import ContactMessageForm
from .models import ActivityLog


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi.')
            return redirect('contact')
        messages.error(request, 'Iltimos, quyidagi xatolarni tuzating.')
    else:
        form = ContactMessageForm()
    return render(request, 'pages/contact.html', {'form': form})


def search(request):
    query = request.GET.get('q', '').strip()
    context = {
        'query': query,
        'companies': [],
        'projects': [],
        'investments': [],
        'news_articles': [],
    }
    if query:
        context['companies'] = Company.objects.filter(
            Q(name__icontains=query) | Q(region__icontains=query) | Q(industry__icontains=query)
        )[:10]
        context['projects'] = Project.objects.select_related('company').filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query)
        )[:10]
        context['investments'] = Investment.objects.select_related('company').filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(sector__icontains=query)
        )[:10]
        context['news_articles'] = News.objects.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query) | Q(content__icontains=query),
            is_published=True,
        )[:10]
    return render(request, 'search/results.html', context)


@login_required
def my_dashboard(request):
    role = get_user_role(request.user)
    context = {
        'role': role,
        'owned_companies_count': 0,
        'owned_projects_count': 0,
        'submitted_investor_applications_count': 0,
        'total_companies': 0,
        'total_projects': 0,
        'total_investments': 0,
        'total_partnership_applications': 0,
        'total_investor_applications': 0,
    }
    if role == 'COMPANY':
        context['owned_companies_count'] = Company.objects.filter(owner=request.user).count()
        context['owned_projects_count'] = Project.objects.filter(
            Q(created_by=request.user) | Q(company__owner=request.user)
        ).distinct().count()
    elif role == 'INVESTOR':
        context['submitted_investor_applications_count'] = InvestorApplication.objects.filter(
            email=request.user.email
        ).count()
    elif role == 'ADMIN':
        context.update({
            'total_companies': Company.objects.count(),
            'total_projects': Project.objects.count(),
            'total_investments': Investment.objects.count(),
            'total_partnership_applications': ProjectApplication.objects.count(),
            'total_investor_applications': InvestorApplication.objects.count(),
        })
    return render(request, 'dashboard/my_dashboard.html', context)


@login_required
@user_passes_test(is_admin)
def system_report_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="system_report.pdf"'

    pdf = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y = height - 72

    pdf.setFont('Helvetica-Bold', 18)
    pdf.drawString(72, y, 'Hududiy sanoat kooperatsiyasi platformasi')
    y -= 28
    pdf.setFont('Helvetica', 12)
    pdf.drawString(72, y, 'Tizim statistikasi hisoboti')
    y -= 36

    rows = [
        ('Jami korxonalar', Company.objects.count()),
        ('Jami loyihalar', Project.objects.count()),
        ('Jami investitsiyalar', Investment.objects.count()),
        ('Hamkorlik arizalari', ProjectApplication.objects.count()),
        ('Investor arizalari', InvestorApplication.objects.count()),
        ('Nashr etilgan yangiliklar', News.objects.filter(is_published=True).count()),
        ('Qoralama yangiliklar', News.objects.filter(is_published=False).count()),
        ('Faollik yozuvlari', ActivityLog.objects.count()),
    ]

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(72, y, 'Ko‘rsatkich')
    pdf.drawString(width - 220, y, 'Qiymat')
    y -= 18
    pdf.line(72, y, width - 72, y)
    y -= 22

    pdf.setFont('Helvetica', 11)
    for label, value in rows:
        pdf.drawString(72, y, label)
        pdf.drawString(width - 220, y, str(value))
        y -= 22

    y -= 20
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(72, y, 'So‘nggi faolliklar')
    y -= 20
    pdf.setFont('Helvetica', 10)
    for activity in ActivityLog.objects.select_related('user')[:8]:
        pdf.drawString(72, y, f'{activity.created_at:%Y-%m-%d} - {activity.description[:80]}')
        y -= 16

    pdf.showPage()
    pdf.save()
    return response
