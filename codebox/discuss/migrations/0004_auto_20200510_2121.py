# Generated by Django 3.0.3 on 2020-05-10 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0003_post_query_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='query_image',
            new_name='queryimage',
        ),
    ]
