# Generated by Django 2.2.27 on 2022-08-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagePlaces', '0010_auto_20220803_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='icon',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
