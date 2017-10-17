# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import restaurants.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_merge_20170930_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='reporter',
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validators.validate_category]),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
