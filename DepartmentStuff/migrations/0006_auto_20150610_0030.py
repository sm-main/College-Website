# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DepartmentStuff', '0005_auto_20150610_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('computer-department', 'computer-department'), ('mechanical-department', 'mechanical-department'), ('electrical-department', 'electrical-department'), ('electronics-department', 'electronics-department'), ('MBA Department', 'mba-department'), ('H&S Department', 'humanities-department')], max_length=23),
            preserve_default=True,
        ),
    ]
