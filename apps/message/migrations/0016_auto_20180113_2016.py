# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0015_auto_20180113_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default='1994-01-01 00:00:00', max_length=20, verbose_name='发送时间'),
        ),
    ]
