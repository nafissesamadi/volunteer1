# Generated by Django 4.2.9 on 2024-04-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_publicplacetype_publicplace_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='url_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='url_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
