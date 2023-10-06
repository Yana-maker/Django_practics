# Generated by Django 4.2.5 on 2023-09-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_material_is_published_material_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='view_count',
            new_name='views_count',
        ),
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
    ]
