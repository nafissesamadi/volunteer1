# Generated by Django 4.2.9 on 2024-05-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0022_alter_applicant_gpa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skilledvolunteer',
            name='job_role',
        ),
        migrations.RemoveField(
            model_name='skilledvolunteer',
            name='offered_skill',
        ),
        migrations.RemoveField(
            model_name='skilledvolunteer',
            name='user',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='special_condition',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='EducationalVolunteer',
        ),
        migrations.DeleteModel(
            name='SkilledVolunteer',
        ),
    ]
