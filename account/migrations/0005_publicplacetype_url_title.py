# Generated by Django 4.2.9 on 2024-04-29 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_city_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicplacetype',
            name='url_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]