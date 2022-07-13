# Generated by Django 2.2.27 on 2022-07-13 08:51

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Way', '0004_way'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_to_way',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='user_to_way',
            name='show',
        ),
        migrations.RemoveField(
            model_name='user_to_way',
            name='way',
        ),
        migrations.RemoveField(
            model_name='way',
            name='GeoJSON_lines',
        ),
        migrations.RemoveField(
            model_name='way',
            name='name_way',
        ),
        migrations.AddField(
            model_name='user_to_way',
            name='id_way',
            field=models.PositiveIntegerField(default=0, verbose_name='id_way'),
        ),
        migrations.AddField(
            model_name='way',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='rating'),
        ),
        migrations.AddField(
            model_name='way',
            name='show',
            field=models.BooleanField(default=False, verbose_name='show'),
        ),
        migrations.AddField(
            model_name='way',
            name='way',
            field=jsonfield.fields.JSONField(default=dict, verbose_name='way'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id_user',
            field=models.PositiveIntegerField(default=0, verbose_name='id_user'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id_way',
            field=models.PositiveIntegerField(default=0, verbose_name='id_way'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='is_deleted'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='user_to_way',
            name='id_user',
            field=models.PositiveIntegerField(default=0, verbose_name='id_user'),
        ),
        migrations.AlterField(
            model_name='user_to_way',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='is_deleted'),
        ),
        migrations.AlterField(
            model_name='way',
            name='id_user',
            field=models.PositiveIntegerField(default=0, verbose_name='id_user'),
        ),
        migrations.AlterField(
            model_name='way',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='is_deleted'),
        ),
        migrations.AlterField(
            model_name='way_to_comm',
            name='id_user',
            field=models.PositiveIntegerField(default=0, verbose_name='id_user'),
        ),
        migrations.AlterField(
            model_name='way_to_comm',
            name='id_way',
            field=models.PositiveIntegerField(default=0, verbose_name='id_way'),
        ),
        migrations.AlterField(
            model_name='way_to_comm',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='is_deleted'),
        ),
    ]
