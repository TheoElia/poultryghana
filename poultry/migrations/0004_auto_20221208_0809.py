# Generated by Django 3.2.16 on 2022-12-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poultry', '0003_auto_20221207_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poultryrecord',
            name='no_of_animals',
        ),
        migrations.AddField(
            model_name='record',
            name='no_of_birds',
            field=models.IntegerField(null=True),
        ),
    ]
