# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-23 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20170622_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phoneno',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
