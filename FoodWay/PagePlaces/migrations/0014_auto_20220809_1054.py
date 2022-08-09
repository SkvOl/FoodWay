# Generated by Django 2.2.27 on 2022-08-09 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagePlaces', '0013_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
