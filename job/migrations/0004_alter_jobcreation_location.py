# Generated by Django 5.1.6 on 2025-02-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_experience_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcreation',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
