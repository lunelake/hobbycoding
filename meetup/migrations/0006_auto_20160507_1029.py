# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-07 10:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0005_auto_20160409_0707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetup',
            options={'ordering': ['-created_date'], 'verbose_name': '밋업', 'verbose_name_plural': '밋업'},
        ),
    ]
