# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=140)),
                ('RollNo', models.CharField(max_length=140)),
                ('Dues', models.CharField(max_length=140)),
                ('Status', models.CharField(max_length=140)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]