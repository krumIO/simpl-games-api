# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-02 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_auto_20160930_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='world',
            options={'ordering': ('pk',), 'verbose_name': 'world', 'verbose_name_plural': 'worlds'},
        ),
    ]
