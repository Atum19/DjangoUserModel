# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-28 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='zipcode',
            field=models.CharField(default='10020', max_length=120),
        ),
    ]
