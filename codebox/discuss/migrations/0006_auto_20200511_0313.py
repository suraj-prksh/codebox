# Generated by Django 3.0.3 on 2020-05-11 03:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0005_auto_20200510_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
