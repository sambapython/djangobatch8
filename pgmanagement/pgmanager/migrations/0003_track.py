# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-15 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgmanager', '0002_room_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=250)),
                ('status_cod', models.IntegerField(blank=True)),
            ],
        ),
    ]