# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DepartmentStuff', '0002_auto_20150516_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmental_snapshot',
            name='department',
            field=models.OneToOneField(to='DepartmentStuff.Department', related_name='stk'),
            preserve_default=True,
        ),
    ]
