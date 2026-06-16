from django.db import models
from django.conf import settings


class Company(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='owned_companies',
    )
    name = models.CharField(max_length=255, db_index=True)
    region = models.CharField(max_length=120, db_index=True)
    industry = models.CharField(max_length=120, db_index=True)
    director = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Korxona'
        verbose_name_plural = 'Korxonalar'
        indexes = [
            models.Index(fields=['region', 'industry']),
        ]

    def __str__(self):
        return self.name
