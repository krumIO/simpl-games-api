# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-30 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0023_auto_20161018_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
