# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20181024_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customername',
            name='location',
            field=models.CharField(blank=True, max_length=501, null=True),
        ),
    ]
