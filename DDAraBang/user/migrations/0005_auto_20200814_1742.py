# Generated by Django 2.2.3 on 2020-08-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_buylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='buylist',
            field=models.CharField(default='', max_length=10000, null=True),
        ),
    ]