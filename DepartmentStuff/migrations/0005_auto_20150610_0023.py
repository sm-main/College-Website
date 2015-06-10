# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DepartmentStuff', '0004_auto_20150610_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=23, choices=[('computer-department', 'computer-department'), ('Mechanical Department', 'Mechanical Department'), ('Electrical Department', 'Electrical Department'), ('Electronics Department', 'Electronics Department'), ('MBA Department', 'MBA Department'), ('H&S Department', 'Humanities Department')]),
            preserve_default=True,
        ),
    ]
