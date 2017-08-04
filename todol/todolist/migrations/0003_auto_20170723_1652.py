# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20170723_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='task',
            name='width_field',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
