# Generated by Django 2.2.27 on 2022-08-02 10:02

import PagePlaces.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagePlaces', '0008_auto_20220802_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageplaces',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to=PagePlaces.models.icon_place),
        ),
        migrations.AlterField(
            model_name='pageplaces',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='pageplaces',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=19, null=True),
        ),
    ]