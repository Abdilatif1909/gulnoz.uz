from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from accounts.models import UserProfile
from companies.models import Company
from core.models import ActivityLog
from investments.models import Investment
from news.models import News
from projects.models import Project


class ProductionReadinessTests(TestCase):
    def setUp(self):
        self.company_user = User.objects.create_user(
            username='company_user',
            password='StrongPass12345',
            email='company@example.com',
        )
        self.company_user.profile.role = UserProfile.Role.COMPANY
        self.company_user.profile.save()

        self.investor_user = User.objects.create_user(
            username='investor_user',
            password='StrongPass12345',
            email='investor@example.com',
        )
        self.investor_user.profile.role = UserProfile.Role.INVESTOR
        self.investor_user.profile.save()

        self.admin_user = User.objects.create_superuser(
            username='admin_user',
            password='StrongPass12345',
            email='admin@example.com',
        )

        self.company = Company.objects.create(
            owner=self.company_user,
            name='Audit Company',
            region='Tashkent',
            industry='Manufacturing',
            director='Audit Director',
            phone='+998 90 000 00 00',
            email='audit-company@example.com',
            description='Audit company description.',
        )
        self.project = Project.objects.create(
            created_by=self.company_user,
            company=self.company,
            title='Audit Project',
            category='Manufacturing',
            budget='100000.00',
            duration_months=12,
            region='Tashkent',
            description='Audit project description.',
            requirements='Audit project requirements.',
        )
        self.investment = Investment.objects.create(
            company=self.company,
            title='Audit Investment',
            sector='Manufacturing',
            required_amount='250000.00',
            expected_roi='12.50',
            investment_period_months=24,
            region='Tashkent',
            description='Audit investment description.',
            benefits='Audit benefits.',
            risks='Audit risks.',
        )
        self.news = News.objects.create(
            title='Audit News',
            slug='audit-news',
            short_description='Audit short description.',
            content='Audit content.',
            author='Audit Author',
            is_published=True,
        )
        ActivityLog.objects.all().delete()

    def test_public_pages_render(self):
        paths = [
            reverse('home'),
            reverse('dashboard:index'),
            reverse('companies:list'),
            reverse('projects:list'),
            reverse('investments:list'),
            reverse('news:list'),
            reverse('news:detail', kwargs={'slug': self.news.slug}),
            reverse('core:search') + '?q=audit',
        ]
        for path in paths:
            with self.subTest(path=path):
                response = self.client.get(path, secure=True)
                self.assertEqual(response.status_code, 200)

    def test_exports_download(self):
        export_names = [
            'companies:export_csv',
            'projects:export_csv',
            'investments:export_csv',
        ]
        for name in export_names:
            with self.subTest(name=name):
                response = self.client.get(reverse(name), secure=True)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response['Content-Type'], 'text/csv')
                self.assertIn('attachment;', response['Content-Disposition'])

    def test_admin_pdf_report_is_protected(self):
        response = self.client.get(reverse('core:system_report_pdf'), secure=True)
        self.assertEqual(response.status_code, 302)

        self.client.force_login(self.admin_user)
        response = self.client.get(reverse('core:system_report_pdf'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_investor_cannot_create_investment(self):
        self.client.force_login(self.investor_user)
        response = self.client.get(reverse('investments:create'), secure=True)
        self.assertEqual(response.status_code, 403)

    def test_login_activity_is_recorded(self):
        logged_in = self.client.login(username='company_user', password='StrongPass12345')
        self.assertTrue(logged_in)
        self.assertTrue(ActivityLog.objects.filter(user=self.company_user, action='LOGIN').exists())
