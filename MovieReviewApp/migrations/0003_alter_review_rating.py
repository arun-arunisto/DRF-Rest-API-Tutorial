# Generated by Django 5.0.3 on 2024-05-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReviewApp', '0002_review_review_time_alter_movie_released_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(),
        ),
    ]