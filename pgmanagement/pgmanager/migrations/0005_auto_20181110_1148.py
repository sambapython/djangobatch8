# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-10 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgmanager', '0004_pg_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgmanager',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
