# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DepartmentStuff', '0003_auto_20150517_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman_message',
            name='department',
            field=models.OneToOneField(related_name='cha', to='DepartmentStuff.Department'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('computer-department', 'Computer Department'), ('Mechanical Department', 'Mechanical Department'), ('Electrical Department', 'Electrical Department'), ('Electronics Department', 'Electronics Department'), ('MBA Department', 'MBA Department'), ('H&S Department', 'Humanities Department')], max_length=23),
            preserve_default=True,
        ),
    ]
