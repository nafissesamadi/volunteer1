# Generated by Django 4.2.9 on 2024-01-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0019_course_book_download_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationallevel',
            name='url_title',
            field=models.CharField(default='elementary', max_length=200),
        ),
        migrations.AddField(
            model_name='grade',
            name='url_title',
            field=models.CharField(default='elementary', max_length=200),
        ),
    ]
