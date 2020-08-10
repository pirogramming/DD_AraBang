# Generated by Django 2.2.9 on 2020-08-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
    ]
