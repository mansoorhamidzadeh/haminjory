# Generated by Django 4.2 on 2023-04-17 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("haminjory", "0005_alter_article_options_category_parent_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "Artilce", "verbose_name_plural": "Articles"},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["parent__id", "-position"]},
        ),
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="articles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]