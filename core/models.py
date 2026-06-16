from django.db import models
from django.conf import settings


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f'{self.full_name} - {self.subject}'


class ActivityLog(models.Model):
    class Action(models.TextChoices):
        LOGIN = 'LOGIN', 'Tizimga kirish'
        COMPANY_CREATED = 'COMPANY_CREATED', 'Korxona yaratildi'
        PROJECT_CREATED = 'PROJECT_CREATED', 'Loyiha yaratildi'
        INVESTMENT_CREATED = 'INVESTMENT_CREATED', 'Investitsiya yaratildi'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='activity_logs',
    )
    action = models.CharField(max_length=40, choices=Action.choices, db_index=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['action', '-created_at']),
        ]

    def __str__(self):
        return self.description
