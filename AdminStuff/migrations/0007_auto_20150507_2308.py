# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminStuff', '0006_department_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department_image',
            old_name='Department_image',
            new_name='department_image',
        ),
    ]
