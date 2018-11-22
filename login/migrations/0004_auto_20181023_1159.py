# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20181023_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='customername',
            name='basic_value',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='branch_name',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='business_segment',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='contact_number',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='contract_job',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='cust_id',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='cust_tier',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='expiry_date',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='premise_type',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
        migrations.AddField(
            model_name='customername',
            name='renewal_date',
            field=models.CharField(blank=True, max_length=251, null=True),
        ),
    ]
