# Generated by Django 3.0.3 on 2020-05-10 21:06

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]