# Generated by Django 3.0.3 on 2020-05-12 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0011_auto_20200512_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
