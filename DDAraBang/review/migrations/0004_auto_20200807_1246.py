# Generated by Django 2.2.3 on 2020-08-07 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_school_gu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='gu',
            field=models.CharField(max_length=25),
        ),
    ]