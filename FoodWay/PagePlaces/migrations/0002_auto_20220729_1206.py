# Generated by Django 2.2.27 on 2022-07-29 09:06

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PagePlaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageplaces',
            options={'verbose_name': 'page places', 'verbose_name_plural': 'page places'},
        ),
        migrations.AlterField(
            model_name='pageplaces',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]