# Generated by Django 5.0.3 on 2024-04-03 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 3, 12, 26, 31, 815247)),
        ),
    ]
