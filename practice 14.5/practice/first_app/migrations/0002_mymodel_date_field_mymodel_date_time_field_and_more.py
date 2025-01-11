# Generated by Django 5.1.3 on 2025-01-10 18:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='date_field',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='date_time_field',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='decimal_field',
            field=models.DecimalField(decimal_places=2, default=5.5, max_digits=5),
        ),
    ]
