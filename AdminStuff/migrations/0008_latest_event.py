# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminStuff', '0007_auto_20150507_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latest_Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_content', models.TextField(max_length=1000, null=True)),
                ('event_files', models.FileField(upload_to='AdminStuff/event_uploads/files')),
                ('event_photo', models.ImageField(upload_to='AdminStuff/event_uploads/photos')),
                ('pub_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
