# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_auto_20150720_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='menu',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
