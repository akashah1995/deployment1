# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170720_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='This is a story about how a boy grew up in the hood'),
            preserve_default=False,
        ),
    ]
