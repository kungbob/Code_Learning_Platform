# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-30 10:22
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_auto_20171230_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='material',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
