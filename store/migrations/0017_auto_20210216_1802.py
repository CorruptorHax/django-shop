# Generated by Django 2.2.15 on 2021-02-16 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_scategory_sproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sproduct',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.SCategory', verbose_name='Катерогия услуг'),
        ),
    ]
