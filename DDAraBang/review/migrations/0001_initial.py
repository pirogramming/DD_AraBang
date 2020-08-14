# Generated by Django 2.2.9 on 2020-08-14 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=25)),
                ('lng', models.CharField(max_length=25)),
                ('gu', models.CharField(default=1, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('gu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery')),
                ('floor', models.CharField(max_length=20)),
                ('advantage', models.TextField(help_text='자신이 생각하는 이 집의 장점을 써주세요.')),
                ('disadvantage', models.TextField(help_text='자신이 생각하는 이 집의 단점을 써주세요.')),
                ('water', models.CharField(max_length=20)),
                ('waterplus', models.CharField(blank=True, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!', max_length=50, null=True)),
                ('light', models.CharField(max_length=20)),
                ('lightplus', models.CharField(blank=True, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!', max_length=50, null=True)),
                ('noise', models.CharField(max_length=20)),
                ('noiseplus', models.CharField(blank=True, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!', max_length=50, null=True)),
                ('security', models.CharField(max_length=20)),
                ('securityplus', models.CharField(blank=True, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!', max_length=50, null=True)),
                ('bug', models.CharField(max_length=20)),
                ('bugplus', models.CharField(blank=True, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!', max_length=50, null=True)),
                ('money', models.CharField(blank=True, help_text='ex)월세에 관리비 따로 5만원 정도 더 나오니 계약할 때 꼭 깎아달라고 하세요!', max_length=50, null=True)),
                ('recommend', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='review.Place')),
            ],
        ),
    ]
