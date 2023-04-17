from django.contrib import admin
from .models import *


def make_publish(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = '1 was updated'
    else:
        message_bit = 'updated'
    modeladmin.message_user(request, "{} {} ".format(rows_updated, message_bit))


def make_draft(modeladmin, reuqest, queryset):
    queryset.update(status='d')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'parent')


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        "thumbnail_tag",
        'slug',
        'publish',
        'status',
        'category_to_str',
    )
    actions = [make_publish, make_draft]
    search_fields = ('title',)
    ordering = ('status', '-publish',)

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category_pub()])

    # category_to_str.short_description = 'دسته بندی '


admin.site.register(Article, ArticleAdmin)
