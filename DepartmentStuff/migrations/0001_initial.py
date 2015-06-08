# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chairman_message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('chairman_name', models.CharField(max_length=300)),
                ('chairman_photo', models.ImageField(upload_to='DepatrmentStuff/chairmanMessage_uploads/images')),
                ('chairman_message', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': "Chairman's message",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('department_name', models.CharField(choices=[('Computer Department', 'Computer Department'), ('Mechanical Department', 'Mechanical Department'), ('Electrical Department', 'Electrical Department'), ('Electronics Department', 'Electronics Department'), ('MBA Department', 'MBA Department'), ('H&S Department', 'Humanities Department')], max_length=23)),
                ('about_department', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departmental_snapshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('department_image', models.ImageField(upload_to='DepatrmentStuff/departmentalSnapshot_uploads/images')),
                ('total_faculty_in_department', models.IntegerField()),
                ('no_of_phd', models.IntegerField()),
                ('no_of_mtech', models.IntegerField()),
                ('average_experience', models.IntegerField()),
                ('no_of_pub_in_journal', models.IntegerField()),
                ('no_of_faculty_dev_programmes_attended', models.IntegerField()),
                ('no_of_labs', models.IntegerField()),
                ('no_of_workshops', models.IntegerField(null=True)),
                ('no_of_lecture_halls', models.IntegerField()),
                ('no_of_confrence_rooms', models.IntegerField()),
                ('no_of_smart_rooms', models.IntegerField()),
                ('no_of_research_labs', models.IntegerField()),
                ('internet_speed', models.CharField(max_length=200)),
                ('no_of_media_projectors', models.IntegerField()),
                ('department', models.ForeignKey(to='DepartmentStuff.Department')),
            ],
            options={
                'verbose_name_plural': 'departmental snapshot',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('faculty_photo', models.ImageField(upload_to='DepatrmentStuff/faculty_uploads/images')),
                ('faculty_name', models.CharField(max_length=300)),
                ('faculty_qualification', models.CharField(max_length=1000)),
                ('faculty_designation', models.CharField(max_length=1000)),
                ('faculty_address', models.CharField(max_length=1000)),
                ('faculty_email', models.EmailField(max_length=75)),
                ('faculty_research_papers', models.TextField()),
                ('faculty_experience', models.TextField()),
                ('department', models.ForeignKey(to='DepartmentStuff.Department')),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chairman_message',
            name='department',
            field=models.OneToOneField(to='DepartmentStuff.Department'),
            preserve_default=True,
        ),
    ]
