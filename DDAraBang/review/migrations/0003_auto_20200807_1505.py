# Generated by Django 2.2.9 on 2020-08-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20200807_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewform',
            name='floor',
            field=models.CharField(choices=[('OUTSIDE', '지상'), ('SEMIINSIDE', '반지하'), ('INSIDE', '지하')], max_length=10),
        ),
    ]