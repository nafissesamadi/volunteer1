# Generated by Django 4.2.9 on 2024-05-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0026_alter_educationalvolunteer_offered_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalvolunteer',
            name='offered_course',
            field=models.ManyToManyField(blank=True, null=True, to='application.coursename'),
        ),
    ]
