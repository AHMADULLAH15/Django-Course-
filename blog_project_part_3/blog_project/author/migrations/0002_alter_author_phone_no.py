# Generated by Django 5.1.3 on 2024-12-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
