import json
import random
from datetime import datetime, timedelta
from pathlib import Path


random.seed(20260613)

BASE_DIR = Path(__file__).resolve().parent

REGIONS = [
    'Tashkent',
    'Samarkand',
    'Bukhara',
    'Andijan',
    'Namangan',
    'Fergana',
    'Navoi',
    'Khorezm',
    'Kashkadarya',
    'Surkhandarya',
    'Jizzakh',
    'Syrdarya',
    'Karakalpakstan',
]

INDUSTRIES = [
    'Manufacturing',
    'Agriculture',
    'IT',
    'Energy',
    'Logistics',
    'Construction',
    'Textile',
    'Chemical Industry',
]

STATUSES_PROJECT = ['open', 'in_progress', 'completed']
STATUSES_INVESTMENT = ['open', 'funded', 'closed']
AUTHORS = ['Industry Desk', 'Investment Desk', 'Digital Economy Desk', 'Analytics Center', 'Regional Development Agency']
FIRST_NAMES = ['Akmal', 'Dilshod', 'Javlon', 'Sardor', 'Oybek', 'Rustam', 'Farhod', 'Nodir', 'Madina', 'Gulbahor', 'Dilnoza', 'Zarina', 'Umida', 'Aziza']
LAST_NAMES = ['Karimov', 'Rakhimov', 'Usmonov', 'Sobirov', 'Muminov', 'Tursunov', 'Ergashev', 'Abdullayev', 'Saidova', 'Yuldasheva', 'Rakhimova', 'Ismailova']
COMPANY_SUFFIXES = ['Cluster', 'Systems', 'Industrial Group', 'Tech Park', 'Logistics Hub', 'Manufacturing', 'Processing', 'Solutions', 'Energy', 'Materials']


def write_json(filename, data):
    path = BASE_DIR / filename
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


def slug_part(value):
    return value.lower().replace(' ', '-').replace("'", '')


def make_companies():
    companies = []
    for index in range(1, 101):
        region = REGIONS[(index - 1) % len(REGIONS)]
        industry = INDUSTRIES[(index * 3) % len(INDUSTRIES)]
        suffix = COMPANY_SUFFIXES[index % len(COMPANY_SUFFIXES)]
        director = f'{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}'
        name = f'{region} {industry} {suffix} {index:03d}'
        companies.append({
            'name': name,
            'region': region,
            'industry': industry,
            'director': director,
            'phone': f'+998 {random.randint(60, 99)} {random.randint(100, 999)} {random.randint(10, 99)} {random.randint(10, 99)}',
            'email': f'info{index:03d}@{slug_part(region)}-{slug_part(industry)}.uz',
            'website': f'https://www.{slug_part(region)}-{slug_part(industry)}-{index:03d}.uz',
            'description': f'{name} is a regional enterprise specializing in {industry.lower()} projects, cooperation partnerships, and digital modernization in {region}.',
        })
    return companies


def make_projects():
    categories = ['Manufacturing', 'Agriculture', 'Logistics', 'IT', 'Energy']
    project_types = ['Modernization', 'Cooperation', 'Expansion', 'Digitalization', 'Supply Chain', 'Automation', 'Export Development']
    projects = []
    for index in range(1, 301):
        region = REGIONS[(index + 2) % len(REGIONS)]
        category = categories[index % len(categories)]
        project_type = project_types[index % len(project_types)]
        title = f'{region} {category} {project_type} Project {index:03d}'
        budget = random.randrange(120000, 2500000, 5000)
        projects.append({
            'title': title,
            'category': category,
            'budget': f'{budget}.00',
            'duration_months': random.randint(6, 48),
            'region': region,
            'description': f'{title} is designed to strengthen regional industrial cooperation, improve productivity, and connect enterprises with reliable partners.',
            'requirements': f'Participants should provide experience in {category.lower()}, operational capacity, transparent documentation, and readiness for joint implementation.',
            'status': STATUSES_PROJECT[index % len(STATUSES_PROJECT)],
        })
    return projects


def make_investments():
    sectors = ['Manufacturing', 'Agriculture', 'Energy', 'Information Technology', 'Transport', 'Construction']
    investment_types = ['Capacity Expansion', 'Equipment Upgrade', 'Infrastructure Program', 'Digital Platform', 'Export Growth', 'Efficiency Project']
    investments = []
    for index in range(1, 151):
        region = REGIONS[(index + 5) % len(REGIONS)]
        sector = sectors[index % len(sectors)]
        title = f'{region} {sector} {investment_types[index % len(investment_types)]} {index:03d}'
        amount = random.randrange(200000, 5000000, 10000)
        roi = round(random.uniform(8.5, 24.5), 2)
        investments.append({
            'title': title,
            'sector': sector,
            'required_amount': f'{amount}.00',
            'expected_roi': f'{roi:.2f}',
            'investment_period_months': random.randint(12, 60),
            'region': region,
            'description': f'{title} offers investors access to a practical regional opportunity in {sector.lower()} with measurable development impact.',
            'benefits': 'Expected benefits include expanded production capacity, improved regional employment, stronger supply chains, and export potential.',
            'risks': 'Key risks include market demand changes, equipment delivery delays, currency fluctuation, and implementation schedule pressure.',
            'status': STATUSES_INVESTMENT[index % len(STATUSES_INVESTMENT)],
        })
    return investments


def make_news():
    topics = ['Digitalization', 'Industry', 'Regional Economy', 'Investment', 'Smart Manufacturing', 'Artificial Intelligence']
    news = []
    start_date = datetime(2025, 1, 1, 9, 0, 0)
    for index in range(1, 201):
        topic = topics[index % len(topics)]
        region = REGIONS[index % len(REGIONS)]
        created_at = start_date + timedelta(days=index * 2, hours=index % 8)
        title = f'{topic} Initiative Expands in {region} Region {index:03d}'
        news.append({
            'title': title,
            'short_description': f'{region} enterprises report new progress in {topic.lower()} and industrial cooperation.',
            'content': f'{title}. Regional companies, investors, and public institutions are coordinating practical measures to improve competitiveness, digital readiness, and cooperation between industrial enterprises. The initiative supports thesis-relevant themes such as regional digitalization, investment attraction, analytics, and smart management.',
            'author': AUTHORS[index % len(AUTHORS)],
            'created_at': created_at.isoformat(),
        })
    return news


def make_activity_logs():
    actions = ['LOGIN', 'COMPANY_CREATED', 'PROJECT_CREATED', 'INVESTMENT_CREATED']
    logs = []
    start_date = datetime(2025, 1, 1, 8, 30, 0)
    for index in range(1, 1001):
        action = actions[index % len(actions)]
        region = REGIONS[index % len(REGIONS)]
        created_at = start_date + timedelta(hours=index * 3)
        logs.append({
            'username': f'system_user_{(index % 25) + 1:02d}',
            'action': action,
            'description': f'{action.replace("_", " ").title()} recorded for {region} regional cooperation workflow #{index:04d}',
            'created_at': created_at.isoformat(),
        })
    return logs


def main():
    write_json('companies.json', make_companies())
    write_json('projects.json', make_projects())
    write_json('investments.json', make_investments())
    write_json('news.json', make_news())
    write_json('activity_logs.json', make_activity_logs())
    print('Generated companies.json: 100')
    print('Generated projects.json: 300')
    print('Generated investments.json: 150')
    print('Generated news.json: 200')
    print('Generated activity_logs.json: 1000')


if __name__ == '__main__':
    main()
