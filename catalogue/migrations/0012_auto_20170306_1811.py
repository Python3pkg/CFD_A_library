# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 18:11


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20170306_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='memberid',
            field=models.IntegerField(editable=False),
        ),
    ]
