# Generated by Django 3.2 on 2022-02-12 22:15

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
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Unread'), (1, 'Read'), (2, 'Replied')], default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.SmallIntegerField(choices=[(0, 'Pending confirmation'), (1, 'Confirmed'), (2, 'Canceled')], default=0)),
                ('comment', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
