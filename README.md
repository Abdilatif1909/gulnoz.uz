# Regional Industry Cooperation Platform

A Django web platform for cooperation between regional industrial enterprises under digitalization conditions. The system helps companies publish cooperation projects and investment opportunities, while investors and partners can discover opportunities and submit applications.

## Purpose

This project is prepared for academic thesis demonstration and PythonAnywhere deployment. It demonstrates a complete server-rendered Django application using SQLite, Django Templates, Bootstrap 5, authentication, role-based access, dashboards, search, and admin management.

## Features

- User registration, login, logout, password validation, and messages
- User roles: Admin, Company, Investor
- Company directory with search, filters, pagination, detail pages, and authenticated CRUD
- Cooperation projects with status tracking and partnership applications
- Investment opportunities with investor interest applications
- News module with slug-based articles and publication control
- Dashboard with statistics and Chart.js visualizations
- User dashboard with role-specific statistics
- Contact form stored in the database
- Global search across companies, projects, investments, and news
- Bootstrap 5 responsive templates
- SQLite database for local development and academic demonstration

## Installation

1. Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Apply migrations.

```bash
python manage.py migrate
```

4. Create an administrator account.

```bash
python manage.py createsuperuser
```

5. Run the development server.

```bash
python manage.py runserver
```

## Database

The project uses SQLite by default:

```text
db.sqlite3
```

Seed data is included through Django migrations for companies, projects, investments, and news articles.

## Admin Panel

The Django admin panel is available at:

```text
/admin/
```

Administrators can manage users, profiles, companies, projects, applications, investments, news, and contact messages.

## Screenshots

Add screenshots here for thesis presentation:

- Home page
- Companies page
- Projects page
- Investments page
- Dashboard charts
- Admin panel

## Deployment Guide

This project is prepared for PythonAnywhere deployment. See [deployment_guide.md](deployment_guide.md) for step-by-step instructions.

## Project Structure

```text
regional_cooperation/
accounts/
companies/
projects/
investments/
news/
dashboard/
core/
templates/
static/
media/
manage.py
requirements.txt
```

## Future Improvements

- Email notifications for applications and contact messages
- Advanced company verification workflow
- Export reports to PDF or Excel
- REST API for mobile or external integrations
- More detailed analytics dashboard
- Production database support with PostgreSQL
