from django.db import migrations


SAMPLE_COMPANIES = [
    {
        'name': 'Tashkent Machine Works',
        'region': 'Tashkent',
        'industry': 'Machinery',
        'director': 'Akmal Karimov',
        'phone': '+998 71 200 10 01',
        'email': 'info@tmw.example.com',
        'website': 'https://tmw.example.com',
        'description': 'Producer of industrial machinery and equipment for regional manufacturing enterprises.',
    },
    {
        'name': 'Samarkand Textile Cluster',
        'region': 'Samarkand',
        'industry': 'Textiles',
        'director': 'Dilnoza Rakhimova',
        'phone': '+998 66 210 20 02',
        'email': 'contact@samtextile.example.com',
        'website': 'https://samtextile.example.com',
        'description': 'Integrated textile manufacturer focused on yarn, fabrics, and finished textile products.',
    },
    {
        'name': 'Fergana Chemical Plant',
        'region': 'Fergana',
        'industry': 'Chemicals',
        'director': 'Javlon Usmonov',
        'phone': '+998 73 220 30 03',
        'email': 'office@ferchem.example.com',
        'website': '',
        'description': 'Chemical production enterprise supplying raw materials and industrial components.',
    },
    {
        'name': 'Andijan Auto Components',
        'region': 'Andijan',
        'industry': 'Automotive',
        'director': 'Nodir Sobirov',
        'phone': '+998 74 230 40 04',
        'email': 'info@andijanauto.example.com',
        'website': 'https://andijanauto.example.com',
        'description': 'Manufacturer of components and subassemblies for the automotive supply chain.',
    },
    {
        'name': 'Bukhara Agro Processing',
        'region': 'Bukhara',
        'industry': 'Food Processing',
        'director': 'Madina Saidova',
        'phone': '+998 65 240 50 05',
        'email': 'hello@bukharaagro.example.com',
        'website': '',
        'description': 'Food processing company specializing in packaged agricultural products.',
    },
    {
        'name': 'Namangan Electronics',
        'region': 'Namangan',
        'industry': 'Electronics',
        'director': 'Sardor Muminov',
        'phone': '+998 69 250 60 06',
        'email': 'sales@namanganelectronics.example.com',
        'website': 'https://namanganelectronics.example.com',
        'description': 'Electronics assembly and service provider for industrial automation systems.',
    },
    {
        'name': 'Navoi Mining Services',
        'region': 'Navoi',
        'industry': 'Mining',
        'director': 'Rustam Tursunov',
        'phone': '+998 79 260 70 07',
        'email': 'info@navoimining.example.com',
        'website': 'https://navoimining.example.com',
        'description': 'Industrial services company supporting mining operations and equipment maintenance.',
    },
    {
        'name': 'Kashkadarya Energy Systems',
        'region': 'Kashkadarya',
        'industry': 'Energy',
        'director': 'Gulbahor Yuldasheva',
        'phone': '+998 75 270 80 08',
        'email': 'contact@kenergy.example.com',
        'website': '',
        'description': 'Energy infrastructure enterprise focused on power systems and regional efficiency projects.',
    },
    {
        'name': 'Khorezm Packaging Solutions',
        'region': 'Khorezm',
        'industry': 'Packaging',
        'director': 'Oybek Abdullayev',
        'phone': '+998 62 280 90 09',
        'email': 'office@khorezmpack.example.com',
        'website': 'https://khorezmpack.example.com',
        'description': 'Packaging producer serving food, textile, and consumer goods manufacturers.',
    },
    {
        'name': 'Surkhandarya Construction Materials',
        'region': 'Surkhandarya',
        'industry': 'Construction Materials',
        'director': 'Farhod Ergashev',
        'phone': '+998 76 290 00 10',
        'email': 'info@surkhanmaterials.example.com',
        'website': '',
        'description': 'Supplier of construction materials for regional infrastructure and industrial projects.',
    },
]


def create_sample_companies(apps, schema_editor):
    Company = apps.get_model('companies', 'Company')
    for company_data in SAMPLE_COMPANIES:
        Company.objects.get_or_create(name=company_data['name'], defaults=company_data)


def remove_sample_companies(apps, schema_editor):
    Company = apps.get_model('companies', 'Company')
    Company.objects.filter(name__in=[company['name'] for company in SAMPLE_COMPANIES]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_companies, remove_sample_companies),
    ]
