from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter

# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'), ('p', 'published')
    )
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها '

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
