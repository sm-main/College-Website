from django.db import models
from django.utils import timezone
import datetime


class Notice(models.Model):
	notice_heading=models.CharField(max_length=200)
	notice_content=models.TextField(max_length = 1000, null = True)
	notice_files=models.FileField(upload_to='AdminStuff/notice_uploads/files')
	notice_photo=models.ImageField(upload_to='AdminStuff/notice_uploads/photos')
	pub_date = datetime.datetime.now()
	def __str__(self):
		return self.notice_heading

class File(models.Model):
	notice=models.ForeignKey('Notice')
	file_title=models.CharField(max_length=200)
	add_file=models.FileField(upload_to='AdminStuff/notice_uploads/files')


class News_and_Event(models.Model):
	news_name=models.CharField(max_length=200)
	news_content=models.TextField(max_length = 1000, null = True)
	news_files=models.FileField(upload_to='AdminStuff/news_uploads/files')
	news_photo=models.ImageField(upload_to='AdminStuff/news_uploads/photos')
	def __str__(self):
		return self.news_name


class Tenders(models.Model):
	tender_name=models.CharField(max_length=200)
	tender_detail=models.TextField()
	tender_files=models.FileField(upload_to='AdminStuff/tender_uploads/files')
	def __str__(self):
		return self.tender_name

class Department_image(models.Model):
	department_name=models.CharField(max_length=200)
	department_image=models.FileField(upload_to='AdminStuff/department-images/photos')
	def __str__(self):
		return self.department_name
		
class Latest_Event(models.Model):
	event_name=models.CharField(max_length=200)
	event_content=models.TextField(max_length=1000,null=True)
	event_files=models.FileField(upload_to='AdminStuff/event_uploads/files')
	event_photo=models.ImageField(upload_to='AdminStuff/event_uploads/photos')
	pub_date=models.DateTimeField()
	def __str__(self):
		return self.event_name

