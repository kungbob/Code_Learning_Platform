# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0005_auto_20180320_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='passed_test_case',
        ),
        migrations.RemoveField(
            model_name='version',
            name='total_test_case',
        ),
    ]
