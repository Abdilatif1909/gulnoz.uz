from django.db import models

from companies.models import Company


class Investment(models.Model):
    class Status(models.TextChoices):
        OPEN = 'open', 'Ochiq'
        FUNDED = 'funded', 'Moliyalashtirilgan'
        CLOSED = 'closed', 'Yopilgan'

    title = models.CharField(max_length=255, db_index=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='investments')
    sector = models.CharField(max_length=120, db_index=True)
    required_amount = models.DecimalField(max_digits=14, decimal_places=2)
    expected_roi = models.DecimalField(max_digits=5, decimal_places=2)
    investment_period_months = models.IntegerField()
    region = models.CharField(max_length=120, db_index=True)
    description = models.TextField()
    benefits = models.TextField()
    risks = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', 'title']
        indexes = [
            models.Index(fields=['sector', 'status']),
            models.Index(fields=['region', 'status']),
        ]

    def __str__(self):
        return self.title


class InvestorApplication(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='applications')
    investor_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(db_index=True)
    investment_amount = models.DecimalField(max_digits=14, decimal_places=2)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.investor_name} - {self.investment.title}'
