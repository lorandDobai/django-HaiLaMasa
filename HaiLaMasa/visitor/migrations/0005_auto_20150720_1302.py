# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0004_auto_20150715_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='picture',
            field=models.ImageField(upload_to='restaurants'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='picture',
            field=models.ImageField(upload_to='menus'),
        ),
    ]
