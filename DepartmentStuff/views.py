from django.shortcuts import render
from .models import *
from django.views.generic import View

# Create your views here.
"""
def departmentPage(request,dept_name):
	dept_name1=dept_name.replace('-',' ')
	department_obj_list=Department.objects.all()
	department_name_list=[x.department_name for x in department_obj_list]
	department_name_list=[x.lower() for x in department_name_list]
	index=0
	for x in range(len(department_name_list)):
		if (department_name_list[x]==dept_name1):
			index=x
			break

	dept_obj=department_obj_list[index]	
	return render(request,'DepartmentStuff/department.html',{'dept_obj':dept_obj,'dept_name1':dept_name1})	"""


def about_dept(request,dept_name):
	dept_name1=dept_name.replace('-',' ')
	department_obj_list=Department.objects.all()
	department_name_list=[x.department_name for x in department_obj_list]
	department_name_list=[x.lower() for x in department_name_list]
	index=0
	for x in range(len(department_name_list)):
		if (department_name_list[x]==dept_name1):
			index=x
			break

	dept_obj=department_obj_list[index]
	return render(request,'DepartmentStuff/about_dept.html',{'dept_obj':dept_obj,'dept_name1':dept_name1})

def chairman_message(request,dept_name):
	dept_name1=dept_name.replace('-',' ')
	department_obj_list=Department.objects.all()
	department_name_list=[x.department_name for x in department_obj_list]
	department_name_list=[x.lower() for x in department_name_list]
	index=0
	for x in range(len(department_name_list)):
		if (department_name_list[x]==dept_name1):
			index=x
			break

	dept_obj=department_obj_list[index]
	return render(request,'DepartmentStuff/chairman_message.html',{'dept_obj':dept_obj,'dept_name1':dept_name1})


	


class DepartmentPage(View):
	department_obj_list=Department.objects.all()
	department_name_list=[x.department_name for x in department_obj_list]
	department_name_list=[x.lower() for x in department_name_list]
	index=0
	def get(self,request,dept_name):
		dept_name1=dept_name.replace('-',' ')
		department_obj_list=Department.objects.all()
		department_name_list=[x.department_name for x in department_obj_list]
		department_name_list=[x.lower() for x in department_name_list]
		index=0
		for x in range(len(department_name_list)):
			if(department_name_list[x]==dept_name1):
				index=x
				break
		dept_obj=department_obj_list[index]
		print (index)
		return render(request,'DepartmentStuff/department.html',{'dept_obj':dept_obj})
"""
class DepartmentPage(DetailView):
	model=Department
	def deptPage(self,dept_name):"""
