# Generated by Django 5.0.6 on 2024-08-13 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advancedMethods', '0009_remove_tripimages_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripimages',
            name='filename',
            field=models.CharField(default=datetime.datetime(2024, 8, 13, 12, 46, 35, 289536), max_length=200),
            preserve_default=False,
        ),
    ]
