# Generated by Django 3.0.6 on 2020-05-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200528_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='outstanding',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
