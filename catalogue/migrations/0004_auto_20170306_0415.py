# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 04:15


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(editable=False),
        ),
    ]
