from decimal import Decimal

from django.db import migrations


SAMPLE_PROJECTS = [
    {
        'title': 'Precision Parts Joint Manufacturing Line',
        'company_name': 'Tashkent Machine Works',
        'category': 'Manufacturing',
        'budget': Decimal('850000.00'),
        'duration_months': 18,
        'region': 'Tashkent',
        'description': 'Launch a shared production line for precision mechanical parts used by regional factories.',
        'requirements': 'Partners should provide machining capacity, quality control specialists, or supply chain support.',
        'status': 'open',
    },
    {
        'title': 'Automotive Sensor Assembly Partnership',
        'company_name': 'Andijan Auto Components',
        'category': 'Manufacturing',
        'budget': Decimal('620000.00'),
        'duration_months': 14,
        'region': 'Andijan',
        'description': 'Create a cooperative assembly process for automotive sensors and electronic subcomponents.',
        'requirements': 'Applicants need electronics assembly experience and stable component sourcing channels.',
        'status': 'in_progress',
    },
    {
        'title': 'Industrial Packaging Modernization',
        'company_name': 'Khorezm Packaging Solutions',
        'category': 'Manufacturing',
        'budget': Decimal('410000.00'),
        'duration_months': 10,
        'region': 'Khorezm',
        'description': 'Modernize packaging production for food, textile, and consumer goods manufacturers.',
        'requirements': 'Partners should contribute packaging design, raw material supply, or distribution access.',
        'status': 'open',
    },
    {
        'title': 'Construction Materials Quality Lab',
        'company_name': 'Surkhandarya Construction Materials',
        'category': 'Manufacturing',
        'budget': Decimal('300000.00'),
        'duration_months': 9,
        'region': 'Surkhandarya',
        'description': 'Establish a shared laboratory for testing construction materials and improving product standards.',
        'requirements': 'Applicants should have laboratory equipment, certification expertise, or engineering staff.',
        'status': 'completed',
    },
    {
        'title': 'Digital Cotton Processing Chain',
        'company_name': 'Samarkand Textile Cluster',
        'category': 'Agriculture',
        'budget': Decimal('720000.00'),
        'duration_months': 16,
        'region': 'Samarkand',
        'description': 'Coordinate cotton processing from farms to textile production using shared digital records.',
        'requirements': 'Partners should include farms, logistics providers, or software teams with traceability experience.',
        'status': 'open',
    },
    {
        'title': 'Agro Product Packaging Hub',
        'company_name': 'Bukhara Agro Processing',
        'category': 'Agriculture',
        'budget': Decimal('540000.00'),
        'duration_months': 12,
        'region': 'Bukhara',
        'description': 'Develop a regional packaging hub for processed agricultural products.',
        'requirements': 'Applicants should provide cold storage, packaging lines, or retail distribution connections.',
        'status': 'in_progress',
    },
    {
        'title': 'Smart Greenhouse Components Supply',
        'company_name': 'Namangan Electronics',
        'category': 'Agriculture',
        'budget': Decimal('260000.00'),
        'duration_months': 8,
        'region': 'Namangan',
        'description': 'Produce and deploy sensors and control components for regional greenhouse operators.',
        'requirements': 'Partners need greenhouse operations knowledge, installation teams, or sensor calibration support.',
        'status': 'open',
    },
    {
        'title': 'Regional Cold Chain Coordination',
        'company_name': 'Bukhara Agro Processing',
        'category': 'Logistics',
        'budget': Decimal('950000.00'),
        'duration_months': 20,
        'region': 'Bukhara',
        'description': 'Build a coordinated cold chain network for food processors and agriculture exporters.',
        'requirements': 'Applicants should operate refrigerated transport, warehouses, or distribution platforms.',
        'status': 'open',
    },
    {
        'title': 'Mining Equipment Spare Parts Network',
        'company_name': 'Navoi Mining Services',
        'category': 'Logistics',
        'budget': Decimal('480000.00'),
        'duration_months': 11,
        'region': 'Navoi',
        'description': 'Organize a regional spare parts network for mining equipment maintenance.',
        'requirements': 'Partners should have inventory systems, transport capacity, or equipment service expertise.',
        'status': 'in_progress',
    },
    {
        'title': 'Textile Export Consolidation Center',
        'company_name': 'Samarkand Textile Cluster',
        'category': 'Logistics',
        'budget': Decimal('690000.00'),
        'duration_months': 15,
        'region': 'Samarkand',
        'description': 'Create a shared export consolidation service for textile producers.',
        'requirements': 'Applicants should support customs documentation, warehousing, transport, or export marketing.',
        'status': 'completed',
    },
    {
        'title': 'Industrial Cooperation Data Portal',
        'company_name': 'Namangan Electronics',
        'category': 'IT',
        'budget': Decimal('380000.00'),
        'duration_months': 10,
        'region': 'Namangan',
        'description': 'Develop a digital portal for matching suppliers, producers, and investment opportunities.',
        'requirements': 'Partners should provide software development, cybersecurity, analytics, or user support capacity.',
        'status': 'open',
    },
    {
        'title': 'Factory IoT Monitoring Pilot',
        'company_name': 'Tashkent Machine Works',
        'category': 'IT',
        'budget': Decimal('450000.00'),
        'duration_months': 12,
        'region': 'Tashkent',
        'description': 'Pilot IoT monitoring for production equipment across partner factories.',
        'requirements': 'Applicants need industrial automation, network deployment, or dashboard development experience.',
        'status': 'in_progress',
    },
    {
        'title': 'Automated Warehouse Software Integration',
        'company_name': 'Khorezm Packaging Solutions',
        'category': 'IT',
        'budget': Decimal('220000.00'),
        'duration_months': 7,
        'region': 'Khorezm',
        'description': 'Integrate warehouse software for inventory tracking and order fulfillment.',
        'requirements': 'Partners should have ERP integration, barcode systems, or warehouse process expertise.',
        'status': 'completed',
    },
    {
        'title': 'Energy Efficiency Retrofit Program',
        'company_name': 'Kashkadarya Energy Systems',
        'category': 'Energy',
        'budget': Decimal('1100000.00'),
        'duration_months': 24,
        'region': 'Kashkadarya',
        'description': 'Retrofit industrial facilities with energy monitoring and efficiency improvements.',
        'requirements': 'Applicants should provide audit services, equipment installation, financing, or engineering support.',
        'status': 'open',
    },
    {
        'title': 'Solar Power Supply for Processing Plants',
        'company_name': 'Fergana Chemical Plant',
        'category': 'Energy',
        'budget': Decimal('760000.00'),
        'duration_months': 18,
        'region': 'Fergana',
        'description': 'Deploy solar power systems for industrial processing plants and auxiliary facilities.',
        'requirements': 'Partners should have solar design, installation teams, maintenance services, or project financing.',
        'status': 'open',
    },
]


def create_sample_projects(apps, schema_editor):
    Company = apps.get_model('companies', 'Company')
    Project = apps.get_model('projects', 'Project')
    companies = {company.name: company for company in Company.objects.all()}

    for project_data in SAMPLE_PROJECTS:
        data = project_data.copy()
        company_name = data.pop('company_name')
        company = companies.get(company_name)
        if company is None:
            continue
        Project.objects.get_or_create(title=data['title'], defaults={**data, 'company': company})


def remove_sample_projects(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    Project.objects.filter(title__in=[project['title'] for project in SAMPLE_PROJECTS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('companies', '0002_seed_companies'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_projects, remove_sample_projects),
    ]
