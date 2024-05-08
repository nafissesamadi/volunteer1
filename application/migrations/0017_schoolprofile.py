# Generated by Django 4.2.9 on 2024-05-07 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_publicplace_district_alter_publicplace_name_and_more'),
        ('application', '0016_delete_schoolprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educational_district', models.CharField(blank=True, max_length=7, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.publicplace')),
                ('school_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.educationallevel')),
            ],
        ),
    ]
