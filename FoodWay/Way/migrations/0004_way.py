# Generated by Django 2.2.27 on 2022-07-13 07:56

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Way', '0003_auto_20220711_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='way',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.PositiveIntegerField(verbose_name='id_user')),
                ('name_way', models.CharField(max_length=30)),
                ('GeoJSON_lines', jsonfield.fields.JSONField(default=dict, verbose_name='GeoJSON_lines')),
                ('is_deleted', models.BooleanField(verbose_name='is_deleted')),
            ],
            options={
                'verbose_name': 'way',
                'verbose_name_plural': 'way',
            },
        ),
    ]
