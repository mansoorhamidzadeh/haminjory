from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'position','parent')


admin.site.register(Category,CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'publish',
        'status',
        'category_to_str',
    )
    search_fields = ('title',)
    ordering = ('status', '-publish',)

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category_pub()])

    # category_to_str.short_description = 'دسته بندی '


admin.site.register(Article, ArticleAdmin)
