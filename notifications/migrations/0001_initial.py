# Generated by Django 3.0.6 on 2020-05-28 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('message_status', models.CharField(choices=[('NEW', 'New Notification'), ('READ', 'Notification Read')], default='NEW', max_length=10)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sending_party', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('time_created',),
            },
        ),
    ]
