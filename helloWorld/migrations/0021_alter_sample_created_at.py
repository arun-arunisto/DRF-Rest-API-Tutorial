# Generated by Django 5.0.3 on 2024-05-21 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0020_alter_sample_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 12, 12, 21, 533961)),
        ),
    ]