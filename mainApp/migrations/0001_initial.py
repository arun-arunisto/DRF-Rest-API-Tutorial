# Generated by Django 5.0.3 on 2024-05-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('endpoints', models.TextField()),
                ('connection', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
