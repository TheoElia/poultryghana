# Generated by Django 3.2.16 on 2022-12-07 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=14, null=True)),
                ('cover_image', models.FileField(null=True, upload_to='farms')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('pen_no', models.CharField(max_length=255, null=True)),
                ('weight_at_layer', models.FloatField(null=True)),
                ('date_received', models.DateField(null=True)),
                ('month', models.CharField(max_length=255, null=True)),
                ('breed', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VetShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=14, null=True)),
                ('cover_image', models.FileField(null=True, upload_to='shops')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.TextField(null=True)),
                ('cover_image', models.FileField(null=True, upload_to='products')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='poultry.vetshop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PoultryRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('culls_plus', models.FloatField(null=True)),
                ('culls_minus', models.FloatField(null=True)),
                ('date', models.DateField(null=True)),
                ('age', models.FloatField(help_text='in weeks', null=True)),
                ('production_type', models.CharField(max_length=255, null=True)),
                ('no_of_animals', models.IntegerField(null=True)),
                ('water', models.FloatField(null=True)),
                ('mortality', models.FloatField(null=True)),
                ('egg_production_morning', models.IntegerField(null=True)),
                ('egg_production_afternoon', models.IntegerField(null=True)),
                ('egg_production_evening', models.IntegerField(null=True)),
                ('medication', models.CharField(max_length=255, null=True)),
                ('remarks', models.TextField(null=True)),
                ('farm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='poultry.farm')),
                ('record', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='weekly_records', to='poultry.record')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
