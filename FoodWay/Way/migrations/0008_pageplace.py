# Generated by Django 2.2.27 on 2022-07-21 07:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Way', '0007_auto_20220713_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagePlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
