# Generated by Django 4.2.5 on 2023-09-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.URLField(max_length=100, verbose_name='адрес'),
        ),
    ]
