# Generated by Django 4.2.9 on 2024-04-28 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_delete_schooltype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituteprofile',
            name='venue_type',
        ),
    ]
