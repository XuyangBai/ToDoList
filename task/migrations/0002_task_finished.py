# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
