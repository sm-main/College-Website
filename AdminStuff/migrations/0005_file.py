# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminStuff', '0004_auto_20150421_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('file_title', models.CharField(max_length=200)),
                ('add_file', models.FileField(upload_to='AdminStuff/notice_uploads/files')),
                ('notice', models.ForeignKey(to='AdminStuff.Notice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
