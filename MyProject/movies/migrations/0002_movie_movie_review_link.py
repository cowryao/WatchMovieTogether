# Generated by Django 3.0.3 on 2020-04-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_review_link',
            field=models.URLField(default=''),
        ),
    ]
