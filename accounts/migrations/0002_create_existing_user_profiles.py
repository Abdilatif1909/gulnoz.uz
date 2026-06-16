from django.db import migrations


def create_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('accounts', 'UserProfile')
    for user in User.objects.all():
        role = 'ADMIN' if user.is_superuser or user.is_staff else 'INVESTOR'
        UserProfile.objects.get_or_create(user=user, defaults={'role': role})


def remove_profiles(apps, schema_editor):
    UserProfile = apps.get_model('accounts', 'UserProfile')
    UserProfile.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_profiles, remove_profiles),
    ]
