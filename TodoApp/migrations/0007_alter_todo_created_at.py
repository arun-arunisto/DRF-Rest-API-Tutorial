# Generated by Django 5.0.6 on 2024-07-01 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0006_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 7, 1, 5, 8, 6, 675780)),
        ),
    ]
