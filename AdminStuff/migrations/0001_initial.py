# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_and_Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('news_name', models.CharField(max_length=200)),
                ('news_content', models.TextField()),
                ('news_files', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/files'), upload_to='')),
                ('news_photo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/photos'), upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('notice_heading', models.CharField(max_length=200)),
                ('notice_content', models.TextField()),
                ('notice_files', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/files'), upload_to='')),
                ('notice_photo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/photos'), upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tenders',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tender_name', models.CharField(max_length=200)),
                ('tender_detail', models.TextField()),
                ('tender_files', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/AdminStuff/files'), upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
