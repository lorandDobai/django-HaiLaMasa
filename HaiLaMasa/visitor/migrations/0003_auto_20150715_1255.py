# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_auto_20150715_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
