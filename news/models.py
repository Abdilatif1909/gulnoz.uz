from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class News(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    author = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', 'title']
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        indexes = [
            models.Index(fields=['is_published', '-created_at']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 2
            while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
