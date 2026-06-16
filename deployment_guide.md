# PythonAnywhere Deployment Guide

## 1. Upload Project

Upload the full project folder to your PythonAnywhere account, for example:

```text
/home/yourusername/regional_cooperation
```

## 2. Create Virtualenv

Open a Bash console on PythonAnywhere:

```bash
cd /home/yourusername/regional_cooperation
python3.10 -m venv .venv
source .venv/bin/activate
```

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

## 4. Configure Environment

Set production values in your PythonAnywhere web app environment or WSGI file:

```python
import os
os.environ["DEBUG"] = "False"
os.environ["SECRET_KEY"] = "replace-with-a-secure-secret-key"
os.environ["ALLOWED_HOSTS"] = "yourusername.pythonanywhere.com,.pythonanywhere.com"
```

## 5. Migrate Database

```bash
python manage.py migrate
python manage.py createsuperuser
```

## 6. Collect Static

```bash
python manage.py collectstatic
```

In the PythonAnywhere Web tab, configure static files:

```text
URL: /static/
Directory: /home/yourusername/regional_cooperation/staticfiles
```

For uploaded media:

```text
URL: /media/
Directory: /home/yourusername/regional_cooperation/media
```

## 7. Configure WSGI

Edit the PythonAnywhere WSGI file:

```python
import os
import sys

path = "/home/yourusername/regional_cooperation"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "regional_cooperation.settings"
os.environ["DEBUG"] = "False"
os.environ["SECRET_KEY"] = "replace-with-a-secure-secret-key"
os.environ["ALLOWED_HOSTS"] = "yourusername.pythonanywhere.com,.pythonanywhere.com"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 8. Reload Web App

Return to the PythonAnywhere Web tab and click **Reload**.

## Useful Commands

```bash
python manage.py check
python manage.py migrate
python manage.py collectstatic
```
