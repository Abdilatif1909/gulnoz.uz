from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver

from companies.models import Company
from investments.models import Investment
from projects.models import Project

from .models import ActivityLog


@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    ActivityLog.objects.create(
        user=user,
        action=ActivityLog.Action.LOGIN,
        description=f'{user.username} tizimga kirdi',
    )


@receiver(post_save, sender=Company)
def log_company_creation(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(
            user=instance.owner,
            action=ActivityLog.Action.COMPANY_CREATED,
            description=f'Korxona yaratildi: {instance.name}',
        )


@receiver(post_save, sender=Project)
def log_project_creation(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(
            user=instance.created_by,
            action=ActivityLog.Action.PROJECT_CREATED,
            description=f'Loyiha yaratildi: {instance.title}',
        )


@receiver(post_save, sender=Investment)
def log_investment_creation(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(
            user=None,
            action=ActivityLog.Action.INVESTMENT_CREATED,
            description=f'Investitsiya yaratildi: {instance.title}',
        )
