import json
from datetime import datetime
from decimal import Decimal
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from companies.models import Company
from core.models import ActivityLog
from investments.models import Investment
from news.models import News
from projects.models import Project


class Command(BaseCommand):
    help = 'Load regional cooperation seed data from JSON files in the data directory.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--data-dir',
            default='data',
            help='Directory containing companies.json, projects.json, investments.json, news.json, and activity_logs.json.',
        )

    def handle(self, *args, **options):
        self.data_dir = Path(options['data_dir'])
        if not self.data_dir.exists():
            raise CommandError(f'Data directory not found: {self.data_dir}')

        with transaction.atomic():
            company_result = self.import_companies()
            project_result = self.import_projects()
            investment_result = self.import_investments()
            news_result = self.import_news()
            activity_result = self.import_activity_logs()

        self.stdout.write(self.style.SUCCESS('Import completed.'))
        self.stdout.write(f"Companies imported: {company_result['created']} skipped: {company_result['skipped']}")
        self.stdout.write(f"Projects imported: {project_result['created']} skipped: {project_result['skipped']}")
        self.stdout.write(f"Investments imported: {investment_result['created']} skipped: {investment_result['skipped']}")
        self.stdout.write(f"News imported: {news_result['created']} skipped: {news_result['skipped']}")
        self.stdout.write(f"Activities imported: {activity_result['created']} skipped: {activity_result['skipped']}")

    def read_json(self, filename):
        path = self.data_dir / filename
        if not path.exists():
            raise CommandError(f'Missing data file: {path}')
        return json.loads(path.read_text(encoding='utf-8'))

    def parse_datetime(self, value):
        parsed = datetime.fromisoformat(value)
        if timezone.is_naive(parsed):
            parsed = timezone.make_aware(parsed, timezone.get_current_timezone())
        return parsed

    def result(self):
        return {'created': 0, 'skipped': 0}

    def import_companies(self):
        result = self.result()
        for item in self.read_json('companies.json'):
            _, created = Company.objects.get_or_create(
                name=item['name'],
                defaults={
                    'region': item['region'],
                    'industry': item['industry'],
                    'director': item['director'],
                    'phone': item['phone'],
                    'email': item['email'],
                    'website': item.get('website', ''),
                    'description': item['description'],
                },
            )
            result['created' if created else 'skipped'] += 1
        self.stdout.write('Companies processed.')
        return result

    def import_projects(self):
        result = self.result()
        companies = list(Company.objects.order_by('id'))
        if not companies:
            raise CommandError('Projects require at least one company. Import companies first.')

        for index, item in enumerate(self.read_json('projects.json')):
            company = self.pick_company(companies, item['region'], index)
            _, created = Project.objects.get_or_create(
                title=item['title'],
                defaults={
                    'company': company,
                    'category': item['category'],
                    'budget': Decimal(str(item['budget'])),
                    'duration_months': item['duration_months'],
                    'region': item['region'],
                    'description': item['description'],
                    'requirements': item['requirements'],
                    'status': item['status'],
                },
            )
            result['created' if created else 'skipped'] += 1
        self.stdout.write('Projects processed.')
        return result

    def import_investments(self):
        result = self.result()
        companies = list(Company.objects.order_by('id'))
        if not companies:
            raise CommandError('Investments require at least one company. Import companies first.')

        for index, item in enumerate(self.read_json('investments.json')):
            company = self.pick_company(companies, item['region'], index)
            _, created = Investment.objects.get_or_create(
                title=item['title'],
                defaults={
                    'company': company,
                    'sector': item['sector'],
                    'required_amount': Decimal(str(item['required_amount'])),
                    'expected_roi': Decimal(str(item['expected_roi'])),
                    'investment_period_months': item['investment_period_months'],
                    'region': item['region'],
                    'description': item['description'],
                    'benefits': item['benefits'],
                    'risks': item['risks'],
                    'status': item['status'],
                },
            )
            result['created' if created else 'skipped'] += 1
        self.stdout.write('Investments processed.')
        return result

    def import_news(self):
        result = self.result()
        for item in self.read_json('news.json'):
            slug = slugify(item['title'])
            article, created = News.objects.get_or_create(
                slug=slug,
                defaults={
                    'title': item['title'],
                    'short_description': item['short_description'],
                    'content': item['content'],
                    'author': item['author'],
                    'is_published': True,
                },
            )
            if created:
                article.created_at = self.parse_datetime(item['created_at'])
                article.save(update_fields=['created_at'])
            result['created' if created else 'skipped'] += 1
        self.stdout.write('News processed.')
        return result

    def import_activity_logs(self):
        result = self.result()
        valid_actions = {choice[0] for choice in ActivityLog.Action.choices}
        for item in self.read_json('activity_logs.json'):
            if item['action'] not in valid_actions:
                result['skipped'] += 1
                continue
            created_at = self.parse_datetime(item['created_at'])
            exists = ActivityLog.objects.filter(
                action=item['action'],
                description=item['description'],
                created_at=created_at,
            ).exists()
            if exists:
                result['skipped'] += 1
                continue
            activity = ActivityLog.objects.create(
                action=item['action'],
                description=item['description'],
            )
            activity.created_at = created_at
            activity.save(update_fields=['created_at'])
            result['created'] += 1
        self.stdout.write('Activities processed.')
        return result

    def pick_company(self, companies, region, index):
        regional_companies = [company for company in companies if company.region == region]
        if regional_companies:
            return regional_companies[index % len(regional_companies)]
        return companies[index % len(companies)]
