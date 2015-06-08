# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminStuff', '0003_auto_20150418_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_and_event',
            name='news_content',
            field=models.TextField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_content',
            field=models.TextField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
