# Generated by Django 5.0.3 on 2024-05-20 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0011_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 12, 42, 29, 355722)),
        ),
    ]
