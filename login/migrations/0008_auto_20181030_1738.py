# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20181026_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='customername',
            name='contract_period_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='contract_period_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='service',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
    ]
