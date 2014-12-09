# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eponym', '0004_carmodeloption'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='options',
            field=models.ManyToManyField(to='eponym.CarModelOption'),
            preserve_default=True,
        ),
    ]
