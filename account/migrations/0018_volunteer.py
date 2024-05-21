# Generated by Django 4.2.9 on 2024-05-11 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_publicplace_city_alter_publicplace_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_degree', models.CharField(blank=True, choices=[('UG', 'Under Graduate'), ('B', 'BACHELOR'), ('M', 'MASTER'), ('PHD', 'PHD')], max_length=10, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married')], max_length=50, null=True)),
                ('work_experience', models.IntegerField(blank=True, null=True)),
                ('bio', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.job')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]