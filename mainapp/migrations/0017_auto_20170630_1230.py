# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-30 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20170630_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manuscript',
            old_name='photo',
            new_name='mdocfile',
        ),
        migrations.AddField(
            model_name='manuscript',
            name='status',
            field=models.CharField(default='Pending', max_length=12),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='mtitle',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
