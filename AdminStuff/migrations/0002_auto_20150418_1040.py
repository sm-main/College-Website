# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('AdminStuff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_and_event',
            name='news_files',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/files/news'), upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news_and_event',
            name='news_photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/photos/news'), upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_files',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/files/notice'), upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/photos/notice'), upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tenders',
            name='tender_files',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/files/tenders'), upload_to=''),
            preserve_default=True,
        ),
    ]
