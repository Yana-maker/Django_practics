# Generated by Django 4.2.5 on 2023-09-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_contacts_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='massage',
            field=models.CharField(max_length=100, verbose_name='краткое описание'),
        ),
    ]
