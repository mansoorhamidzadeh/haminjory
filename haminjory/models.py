from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.html import format_html

from extensions.utils import jalali_converter


# Create your models here.

class ArticleManager(models.Manager):
    def publish(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children')
    title = models.CharField(max_length=100, verbose_name='title')
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['parent__id', '-position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'), ('p', 'published')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='auther')
    title = models.CharField(max_length=100, verbose_name='title')
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, verbose_name='category', related_name='articles')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Artilce'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def thumbnail_tag(self):
        return format_html("<img with=100 height=75 src='{}'/>".format(self.thumbnail.url))

    # def jpublish(self):
    #     return jalali_converter(self.publish)
    def category_pub(self):
        return self.category.filter(status=True)

    objects = ArticleManager()
