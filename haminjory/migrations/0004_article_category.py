# Generated by Django 4.2 on 2023-04-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("haminjory", "0003_category_alter_article_options_alter_article_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ManyToManyField(
                to="haminjory.category", verbose_name="دسته بندی "
            ),
        ),
    ]
