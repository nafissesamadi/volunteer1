# Generated by Django 4.2.9 on 2024-01-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_remove_educationalvolunteer_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalvolunteer',
            name='offered_course',
            field=models.ManyToManyField(blank=True, null=True, to='application.coursename'),
        ),
    ]
