# Generated by Django 3.2.16 on 2022-12-07 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poultry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='farm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='poultry.farm'),
        ),
        migrations.AlterField(
            model_name='poultryrecord',
            name='farm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record_records', to='poultry.farm'),
        ),
    ]