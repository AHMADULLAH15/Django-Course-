# Generated by Django 5.1.3 on 2025-01-15 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_phone_no'),
        ('post', '0002_alter_post_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
