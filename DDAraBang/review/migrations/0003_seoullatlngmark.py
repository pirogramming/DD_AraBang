# Generated by Django 3.1.1 on 2020-09-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_reviewform_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoulLatLngMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
            ],
        ),
    ]
