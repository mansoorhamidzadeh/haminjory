from django.contrib import admin
from .models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'jpublish',
        'status',
    )
    search_fields = ('title',)
    ordering = ('status','-publish',)
admin.site.register(Article,ArticleAdmin)