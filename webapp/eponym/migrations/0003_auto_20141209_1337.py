# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eponym', '0002_auto_20141209_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodeloption',
            name='model',
        ),
        migrations.DeleteModel(
            name='CarModelOption',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
