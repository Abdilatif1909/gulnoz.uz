from django.db import migrations
from django.utils.text import slugify


SAMPLE_NEWS = [
    {
        'title': 'Regional Enterprises Accelerate Digital Transformation',
        'short_description': 'Industrial enterprises are adopting shared digital tools to improve coordination and productivity.',
        'content': 'Regional companies are increasing investment in digital workflows, supplier databases, and production monitoring systems. These initiatives support faster cooperation between manufacturers, logistics providers, and investors.',
        'author': 'Platform Editorial Team',
    },
    {
        'title': 'Smart Manufacturing Pilots Expand Across Industrial Zones',
        'short_description': 'Factories are testing connected sensors and digital dashboards for production management.',
        'content': 'Smart manufacturing pilots are helping enterprises monitor equipment performance, reduce downtime, and improve planning. The first results show stronger collaboration between machinery producers and electronics companies.',
        'author': 'Industry Desk',
    },
    {
        'title': 'Artificial Intelligence Supports Industrial Planning',
        'short_description': 'AI-based tools are being introduced for demand forecasting and equipment maintenance planning.',
        'content': 'Artificial intelligence is becoming a practical tool for regional industry. Companies are exploring forecasting, maintenance scheduling, and quality control use cases that can improve operational decisions.',
        'author': 'Technology Desk',
    },
    {
        'title': 'Investment Interest Grows in Energy Efficiency Projects',
        'short_description': 'Investors are showing stronger interest in energy-saving upgrades for industrial facilities.',
        'content': 'Energy efficiency remains one of the most attractive investment directions for regional enterprises. Retrofit projects can reduce costs while supporting more resilient industrial operations.',
        'author': 'Investment Desk',
    },
    {
        'title': 'Regional Economy Benefits from Supplier Cooperation',
        'short_description': 'Local supplier networks are helping companies reduce delays and strengthen production chains.',
        'content': 'Cooperation between regional suppliers and producers is improving access to materials, services, and logistics capacity. These links support a more stable industrial economy.',
        'author': 'Economy Desk',
    },
    {
        'title': 'Digital Platforms Improve Access to Partnership Opportunities',
        'short_description': 'Online listings are making cooperation projects easier to discover and evaluate.',
        'content': 'Digital platforms allow companies to publish project needs, investment opportunities, and contact information in one place. This improves transparency and shortens the time needed to identify partners.',
        'author': 'Platform Editorial Team',
    },
    {
        'title': 'Manufacturers Explore Joint Production Lines',
        'short_description': 'Industrial companies are using cooperation projects to share production capacity.',
        'content': 'Joint production lines can help regional companies reduce capital pressure and serve larger orders. Machinery, automotive, and packaging producers are among the most active participants.',
        'author': 'Industry Desk',
    },
    {
        'title': 'Agriculture and Processing Companies Build Digital Links',
        'short_description': 'Agro-processing enterprises are improving traceability and storage planning through digital tools.',
        'content': 'Digital links between farms, processors, and logistics providers can reduce waste and improve export readiness. Traceability is becoming a priority for higher-value markets.',
        'author': 'Economy Desk',
    },
    {
        'title': 'Investors Review Regional Transport Infrastructure Needs',
        'short_description': 'Transport and logistics opportunities are gaining attention from private investors.',
        'content': 'Regional transport projects can improve shipment reliability for industrial enterprises. Investors are reviewing opportunities in fleet modernization, warehouses, and consolidation hubs.',
        'author': 'Investment Desk',
    },
    {
        'title': 'Industrial Data Helps Companies Compare Cooperation Options',
        'short_description': 'Structured company and project data can make cooperation decisions more reliable.',
        'content': 'Better data allows enterprises to compare regions, industries, budgets, and project status. This supports more informed decisions for both companies and investors.',
        'author': 'Technology Desk',
    },
    {
        'title': 'AI Quality Control Tools Enter Pilot Stage',
        'short_description': 'Manufacturers are piloting computer vision and AI-supported quality checks.',
        'content': 'AI quality control tools can help factories detect defects earlier and reduce manual inspection pressure. Early pilots focus on textiles, packaging, and machinery components.',
        'author': 'Technology Desk',
    },
    {
        'title': 'Regional Investment Projects Target Export Growth',
        'short_description': 'New investment opportunities are focused on production capacity and export logistics.',
        'content': 'Export-oriented investment projects are being prepared in manufacturing, textiles, energy, and transport. These projects aim to expand production and improve delivery reliability.',
        'author': 'Investment Desk',
    },
    {
        'title': 'Construction Materials Producers Modernize Operations',
        'short_description': 'Construction suppliers are investing in new equipment and quality testing capabilities.',
        'content': 'Modern construction materials production supports infrastructure growth and industrial development. Producers are focusing on quality, capacity, and regional distribution.',
        'author': 'Industry Desk',
    },
    {
        'title': 'Digitalization Creates New Roles in Industrial Enterprises',
        'short_description': 'Companies are creating roles for data, automation, and digital project coordination.',
        'content': 'As industrial digitalization expands, companies need staff who can manage data systems, automation tools, and digital cooperation workflows. Training remains a key priority.',
        'author': 'Platform Editorial Team',
    },
    {
        'title': 'Regional Cooperation Strengthens Smart Manufacturing Ecosystem',
        'short_description': 'Manufacturers, IT providers, and investors are forming a more connected industrial ecosystem.',
        'content': 'Smart manufacturing requires cooperation between equipment suppliers, software providers, and production companies. Regional coordination can accelerate adoption and reduce implementation risks.',
        'author': 'Industry Desk',
    },
]


def create_sample_news(apps, schema_editor):
    News = apps.get_model('news', 'News')
    for article in SAMPLE_NEWS:
        slug = slugify(article['title'])
        News.objects.get_or_create(
            slug=slug,
            defaults={
                **article,
                'slug': slug,
                'is_published': True,
            },
        )


def remove_sample_news(apps, schema_editor):
    News = apps.get_model('news', 'News')
    News.objects.filter(slug__in=[slugify(article['title']) for article in SAMPLE_NEWS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_news, remove_sample_news),
    ]
