# Generated by Django 4.2.9 on 2024-05-05 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_publicplace_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicplace',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.publicplacetype'),
            preserve_default=False,
        ),
    ]
