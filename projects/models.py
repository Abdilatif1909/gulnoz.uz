from django.db import models
from django.conf import settings

from companies.models import Company


class Project(models.Model):
    class Status(models.TextChoices):
        OPEN = 'open', 'Ochiq'
        IN_PROGRESS = 'in_progress', 'Jarayonda'
        COMPLETED = 'completed', 'Yakunlangan'

    title = models.CharField(max_length=255, db_index=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='created_projects',
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects')
    category = models.CharField(max_length=120, db_index=True)
    budget = models.DecimalField(max_digits=14, decimal_places=2)
    duration_months = models.IntegerField()
    region = models.CharField(max_length=120, db_index=True)
    description = models.TextField()
    requirements = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', 'title']
        indexes = [
            models.Index(fields=['category', 'status']),
            models.Index(fields=['region', 'status']),
        ]

    def __str__(self):
        return self.title


class ProjectApplication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications')
    applicant_company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(db_index=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.applicant_company_name} - {self.project.title}'
