# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-24 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0006_cluster_character_skill'),
        ('version', '0007_version_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='cluster',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cluster.Cluster'),
            preserve_default=False,
        ),
    ]
