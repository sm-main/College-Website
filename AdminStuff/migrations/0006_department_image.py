# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminStuff', '0005_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department_image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('department_name', models.CharField(max_length=200)),
                ('Department_image', models.FileField(upload_to='AdminStuff/department-images/photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
