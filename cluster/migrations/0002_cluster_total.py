# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]