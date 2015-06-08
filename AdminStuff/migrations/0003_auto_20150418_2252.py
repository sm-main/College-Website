# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminStuff', '0002_auto_20150418_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_and_event',
            name='news_files',
            field=models.FileField(upload_to='AdminStuff/news_uploads/files'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news_and_event',
            name='news_photo',
            field=models.ImageField(upload_to='AdminStuff/news_uploads/photos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_files',
            field=models.FileField(upload_to='AdminStuff/notice_uploads/files'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_photo',
            field=models.ImageField(upload_to='AdminStuff/notice_uploads/photos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tenders',
            name='tender_files',
            field=models.FileField(upload_to='AdminStuff/tender_uploads/files'),
            preserve_default=True,
        ),
    ]
