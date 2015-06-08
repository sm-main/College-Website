# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DepartmentStuff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmental_snapshot',
            name='department',
            field=models.OneToOneField(to='DepartmentStuff.Department'),
            preserve_default=True,
        ),
    ]
