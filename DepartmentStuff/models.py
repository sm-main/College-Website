from django.db import models

class Department(models.Model):
	DEPARTMENT_LIST=(
		('computer-department','computer-department'),
		('mechanical-department','mechanical-department'),
		('electrical-department','electrical-department'),
		('electronics-department','electronics-department'),
		('MBA Department','mba-department'),	
		('H&S Department','humanities-department')
		)
	department_name=models.CharField(max_length=23,choices=DEPARTMENT_LIST,null=False)
	about_department=models.TextField(null=True)
	def __str__(self):
		return self.department_name
	

class Departmental_snapshot(models.Model):
	department=models.OneToOneField(Department,related_name='stk')
	department_image=models.ImageField(upload_to='DepatrmentStuff/departmentalSnapshot_uploads/images')#pending...................
	total_faculty_in_department=models.IntegerField()
	no_of_phd=models.IntegerField()
	no_of_mtech=models.IntegerField()
	average_experience=models.IntegerField()
	no_of_pub_in_journal=models.IntegerField()
	no_of_faculty_dev_programmes_attended=models.IntegerField()
	no_of_labs=models.IntegerField()
	no_of_workshops=models.IntegerField(null=True)
	no_of_lecture_halls=models.IntegerField()
	no_of_confrence_rooms=models.IntegerField()
	no_of_smart_rooms=models.IntegerField()
	no_of_research_labs=models.IntegerField()
	internet_speed=models.CharField(max_length=200)
	no_of_media_projectors=models.IntegerField()
	class Meta:
		verbose_name_plural="departmental snapshot"
	def __str__(self):
		return "Departmental snapshot of "+self.department.department_name


class Faculty(models.Model):
	department=models.ForeignKey(Department,related_name='fac')
	faculty_photo=models.ImageField(upload_to='DepatrmentStuff/faculty_uploads/images')#PENDING........................
	faculty_name=models.CharField(max_length=300)
	faculty_qualification=models.CharField(max_length=1000)
	faculty_designation=models.CharField(max_length=1000)
	faculty_address=models.CharField(max_length=1000)
	faculty_email=models.EmailField()
	faculty_research_papers=models.TextField()
	faculty_experience=models.TextField()
	def __str__(self):
		return self.faculty_name
	class Meta:
		verbose_name_plural="Faculties"

class Chairman_message(models.Model):
	department=models.OneToOneField(Department,related_name='cha')	
	chairman_name=models.CharField(max_length=300)
	chairman_photo=models.ImageField(upload_to='DepatrmentStuff/chairmanMessage_uploads/images')#PENDING.......................
	chairman_message=models.TextField(null=True)
	class Meta:
		verbose_name_plural="Chairman's message"
	def __str__(self):
		return "chairman's message of "+self.department.department_name		