# Generated by Django 4.2.9 on 2024-04-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_publicplacetype_url_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicplace',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
