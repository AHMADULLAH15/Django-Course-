# Generated by Django 5.1.3 on 2025-01-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/media/uploads/'),
        ),
    ]
