# Generated by Django 5.0.6 on 2024-06-17 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifyApp', '0003_alter_album_created_at_alter_tracks_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateField(default=datetime.date(2024, 6, 17)),
        ),
        migrations.AlterField(
            model_name='tracks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 17, 9, 35, 33, 150550)),
        ),
    ]
