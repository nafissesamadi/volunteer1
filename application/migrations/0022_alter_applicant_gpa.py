# Generated by Django 4.2.9 on 2024-05-08 08:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_applicant_is_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
    ]