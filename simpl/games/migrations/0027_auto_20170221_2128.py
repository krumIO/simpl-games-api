# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-21 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0026_auto_20170210_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scenario',
            old_name='creator_user',
            new_name='runuser',
        ),
    ]