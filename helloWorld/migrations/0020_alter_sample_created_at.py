# Generated by Django 5.0.3 on 2024-05-20 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0019_alter_sample_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 20, 12, 42, 29, 351721)),
        ),
    ]