# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0009_auto_20150722_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='picture',
        ),
    ]
