from decimal import Decimal

from django.db import migrations


SAMPLE_INVESTMENTS = [
    {
        'title': 'CNC Equipment Expansion',
        'company_name': 'Tashkent Machine Works',
        'sector': 'Manufacturing',
        'required_amount': Decimal('1200000.00'),
        'expected_roi': Decimal('18.50'),
        'investment_period_months': 36,
        'region': 'Tashkent',
        'description': 'Investment in CNC machines to expand production of industrial mechanical components.',
        'benefits': 'Higher production capacity, export potential, and stable demand from regional manufacturers.',
        'risks': 'Equipment import delays and fluctuating raw material prices.',
        'status': 'open',
    },
    {
        'title': 'Automotive Components Mold Facility',
        'company_name': 'Andijan Auto Components',
        'sector': 'Manufacturing',
        'required_amount': Decimal('950000.00'),
        'expected_roi': Decimal('16.00'),
        'investment_period_months': 30,
        'region': 'Andijan',
        'description': 'Facility for producing molds and tooling for automotive component suppliers.',
        'benefits': 'Reduced import dependence and improved delivery time for local automotive producers.',
        'risks': 'Technology transfer complexity and skilled labor shortages.',
        'status': 'funded',
    },
    {
        'title': 'Agro Processing Cold Storage',
        'company_name': 'Bukhara Agro Processing',
        'sector': 'Agriculture',
        'required_amount': Decimal('780000.00'),
        'expected_roi': Decimal('14.25'),
        'investment_period_months': 28,
        'region': 'Bukhara',
        'description': 'Cold storage expansion for processed fruits, vegetables, and packaged food products.',
        'benefits': 'Reduced spoilage, longer sales cycles, and stronger export readiness.',
        'risks': 'Energy cost increases and seasonal supply variation.',
        'status': 'open',
    },
    {
        'title': 'Cotton Fiber Traceability Program',
        'company_name': 'Samarkand Textile Cluster',
        'sector': 'Agriculture',
        'required_amount': Decimal('520000.00'),
        'expected_roi': Decimal('12.75'),
        'investment_period_months': 20,
        'region': 'Samarkand',
        'description': 'Digital traceability program connecting cotton suppliers with textile production lines.',
        'benefits': 'Improved quality control and better access to compliance-sensitive export buyers.',
        'risks': 'Supplier onboarding delays and data quality issues.',
        'status': 'open',
    },
    {
        'title': 'Industrial Solar Power Package',
        'company_name': 'Kashkadarya Energy Systems',
        'sector': 'Energy',
        'required_amount': Decimal('1500000.00'),
        'expected_roi': Decimal('19.00'),
        'investment_period_months': 42,
        'region': 'Kashkadarya',
        'description': 'Solar generation packages for industrial facilities with high daytime energy demand.',
        'benefits': 'Lower operating costs and long-term energy resilience for industrial customers.',
        'risks': 'Grid connection approvals and currency-sensitive equipment prices.',
        'status': 'open',
    },
    {
        'title': 'Energy Efficient Chemical Processing',
        'company_name': 'Fergana Chemical Plant',
        'sector': 'Energy',
        'required_amount': Decimal('870000.00'),
        'expected_roi': Decimal('15.50'),
        'investment_period_months': 32,
        'region': 'Fergana',
        'description': 'Upgrade processing equipment to reduce energy use and improve production stability.',
        'benefits': 'Lower energy consumption, improved margins, and reduced downtime.',
        'risks': 'Installation interruption and technical commissioning delays.',
        'status': 'closed',
    },
    {
        'title': 'Industrial IoT Monitoring Platform',
        'company_name': 'Namangan Electronics',
        'sector': 'Information Technology',
        'required_amount': Decimal('640000.00'),
        'expected_roi': Decimal('21.00'),
        'investment_period_months': 24,
        'region': 'Namangan',
        'description': 'Development of IoT monitoring software and hardware kits for regional factories.',
        'benefits': 'Recurring software revenue and scalable deployment across manufacturing sites.',
        'risks': 'Cybersecurity requirements and customer adoption speed.',
        'status': 'open',
    },
    {
        'title': 'Warehouse Automation Software',
        'company_name': 'Khorezm Packaging Solutions',
        'sector': 'Information Technology',
        'required_amount': Decimal('410000.00'),
        'expected_roi': Decimal('17.25'),
        'investment_period_months': 18,
        'region': 'Khorezm',
        'description': 'Software platform for warehouse automation, barcode tracking, and dispatch planning.',
        'benefits': 'Operational efficiency and potential licensing to partner warehouses.',
        'risks': 'Integration complexity with legacy inventory systems.',
        'status': 'funded',
    },
    {
        'title': 'Mining Equipment Logistics Fleet',
        'company_name': 'Navoi Mining Services',
        'sector': 'Transport',
        'required_amount': Decimal('1350000.00'),
        'expected_roi': Decimal('16.80'),
        'investment_period_months': 40,
        'region': 'Navoi',
        'description': 'Specialized transport fleet for mining equipment and industrial spare parts.',
        'benefits': 'Strong demand from mining operations and high utilization potential.',
        'risks': 'Fuel price volatility and maintenance cost exposure.',
        'status': 'open',
    },
    {
        'title': 'Regional Textile Export Transport Hub',
        'company_name': 'Samarkand Textile Cluster',
        'sector': 'Transport',
        'required_amount': Decimal('920000.00'),
        'expected_roi': Decimal('13.90'),
        'investment_period_months': 34,
        'region': 'Samarkand',
        'description': 'Transport and consolidation hub for textile exports and interregional shipments.',
        'benefits': 'Reduced logistics costs and faster export preparation for regional producers.',
        'risks': 'Customs process delays and fluctuating export volumes.',
        'status': 'open',
    },
    {
        'title': 'Modern Building Materials Line',
        'company_name': 'Surkhandarya Construction Materials',
        'sector': 'Construction',
        'required_amount': Decimal('700000.00'),
        'expected_roi': Decimal('15.20'),
        'investment_period_months': 26,
        'region': 'Surkhandarya',
        'description': 'New production line for modern construction materials used in regional infrastructure.',
        'benefits': 'Growing construction demand and opportunities in public infrastructure projects.',
        'risks': 'Demand cycles and cement/raw material cost pressure.',
        'status': 'open',
    },
    {
        'title': 'Industrial Packaging Warehouse Buildout',
        'company_name': 'Khorezm Packaging Solutions',
        'sector': 'Construction',
        'required_amount': Decimal('560000.00'),
        'expected_roi': Decimal('12.50'),
        'investment_period_months': 22,
        'region': 'Khorezm',
        'description': 'Warehouse buildout to support packaging materials storage and distribution.',
        'benefits': 'Improved fulfillment speed and stronger supply reliability for industrial clients.',
        'risks': 'Construction timeline delays and occupancy permit requirements.',
        'status': 'closed',
    },
]


def create_sample_investments(apps, schema_editor):
    Company = apps.get_model('companies', 'Company')
    Investment = apps.get_model('investments', 'Investment')
    companies = {company.name: company for company in Company.objects.all()}

    for investment_data in SAMPLE_INVESTMENTS:
        data = investment_data.copy()
        company_name = data.pop('company_name')
        company = companies.get(company_name)
        if company is None:
            continue
        Investment.objects.get_or_create(title=data['title'], defaults={**data, 'company': company})


def remove_sample_investments(apps, schema_editor):
    Investment = apps.get_model('investments', 'Investment')
    Investment.objects.filter(title__in=[investment['title'] for investment in SAMPLE_INVESTMENTS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('companies', '0002_seed_companies'),
        ('investments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_investments, remove_sample_investments),
    ]
