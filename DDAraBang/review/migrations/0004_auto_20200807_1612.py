# Generated by Django 2.2.9 on 2020-08-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20200807_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewform',
            name='bug',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reviewform',
            name='floor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reviewform',
            name='light',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reviewform',
            name='noise',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reviewform',
            name='recommend',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reviewform',
            name='security',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reviewform',
            name='water',
            field=models.CharField(max_length=20),
        ),
    ]