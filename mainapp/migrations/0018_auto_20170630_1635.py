# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-30 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20170630_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuscript',
            name='mabstract',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='mtitle',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
