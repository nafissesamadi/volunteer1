# Generated by Django 4.2.9 on 2024-05-07 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_publicplace_district_alter_publicplace_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicplace',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.city'),
        ),
        migrations.AlterField(
            model_name='publicplace',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.province'),
        ),
    ]
