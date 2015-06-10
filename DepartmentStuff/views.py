from django.shortcuts import render
from .models import *
from django.views.generic import View
from django.core.urlresolvers import reverse

# Create your views here.
department_obj_list=Department.objects.all()
#dept_name1=None
department_name_list=[x.department_name for x in department_obj_list]
#dept_obj=None

def departmentPage(request,dept_name):
	dept_name1=dept_name
	"""
	index=0
	for x in range(len(department_name_list)):
		if (department_name_list[x]==dept_name1):
			index=x
			break
			"""
	index=repetitionStuff(dept_name1)
	dept_obj=department_obj_list[index]	
	return render(request,'DepartmentStuff/department.html',{'dept_obj':dept_obj,'dept_name1':dept_name1})	


def about_dept(request,dept_name):
	dept_name1=dept_name
	"""
	index=0
	for x in range(len(department_name_list)):
		if (department_name_list[x]==dept_name1):
			index=x
			break
			"""
	index=repetitionStuff(dept_name1)		
	dept_obj=department_obj_list[index]
	return render(request,'DepartmentStuff/about_dept.html',{'dept_obj':dept_obj,'dept_name1':dept_name1})

def chairman_message(request,dept_name):
	dept_name1=dept_name
	"""
	index=0
	for x in range(len(department_name_list)):
		if (department_name_list[x]==dept_name1):
			index=x
			break"""
	index=repetitionStuff(dept_name1)		
	dept_obj=department_obj_list[index]
	return render(request,'DepartmentStuff/chairman_message.html',{'dept_obj':dept_obj,'dept_name1':dept_name1})

def faculty(request,dept_name):
	dept_name1=dept_name
	"""
	index=0
	for x in range(len(department_name_list)):
		if(department_name_list[x]==dept_name1):
			index=x
			break
			"""
	index=repetitionStuff(dept_name1)		
	dept_obj=department_obj_list[index]
	faculty_list=dept_obj.fac.all()
	return render(request,'DepartmentStuff/faculty.html',{'dept_obj':dept_obj,'dept_name1':dept_name1,'faculty_list':faculty_list})
	
def faculty_detail(request,dept_name):
	dept_name1=dept_name
	index=repetitionStuff(dept_name1)
	dept_obj=department_obj_list[index]
	faculty_list=dept_obj.fac.all()
	return render(request,'DepartmentStuff/facultyDetail.html',{'dept_obj':dept_obj,'dept_name1':dept_name1,'faculty_list':faculty_list})

def repetitionStuff(dept_name):
	dept_name1=dept_name
	index=0
	for x in range(len(department_name_list)):
		if (department_name_list[x]==dept_name1):
			index=x
			break
	return index


