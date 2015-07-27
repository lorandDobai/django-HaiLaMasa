# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0003_auto_20150715_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='building',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street',
        ),
        migrations.AddField(
            model_name='address',
            name='latitude',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=13),
        ),
        migrations.AddField(
            model_name='address',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=13),
        ),
    ]
