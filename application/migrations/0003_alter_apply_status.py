# Generated by Django 5.1.6 on 2025-02-19 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_apply_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='in_progress', max_length=20),
        ),
    ]
