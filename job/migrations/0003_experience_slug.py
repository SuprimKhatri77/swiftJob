# Generated by Django 5.1.6 on 2025-02-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_skill_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
