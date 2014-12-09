# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eponym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(to='eponym.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='carbrand',
            name='company',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='year',
            field=models.PositiveIntegerField(default=1900),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(to='eponym.Brand'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='CarBrand',
        ),
    ]
