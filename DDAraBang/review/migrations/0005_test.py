# Generated by Django 2.2.3 on 2020-08-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20200807_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=25)),
            ],
        ),
    ]
