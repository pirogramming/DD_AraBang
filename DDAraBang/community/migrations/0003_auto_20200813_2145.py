# Generated by Django 2.2.9 on 2020-08-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20200813_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]