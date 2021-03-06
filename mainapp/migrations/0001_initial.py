# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-05 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PubSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('books_wrote', models.IntegerField(max_length=1000)),
                ('journal_wrote', models.IntegerField(max_length=1000)),
                ('address', models.TextField(max_length=2000)),
                ('website', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserSignup', unique=True),
        ),
    ]
