# Generated by Django 2.2.15 on 2020-08-11 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200811_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
    ]
