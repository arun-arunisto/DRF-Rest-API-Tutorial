# Generated by Django 5.0.6 on 2024-08-16 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifyApp', '0011_alter_tracks_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateField(default=datetime.date(2024, 8, 16)),
        ),
        migrations.AlterField(
            model_name='tracks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 16, 15, 20, 48, 619746)),
        ),
    ]
