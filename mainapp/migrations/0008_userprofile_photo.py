# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-23 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20170623_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='/user/image/'),
        ),
    ]
