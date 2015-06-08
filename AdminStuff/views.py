from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import *

def home(request):
	notice_list1=Notice.objects.filter(pk__gt=1)[:3]
	notice_list2=Notice.objects.filter(pk__gt=1)[3:]
	departments=Department_image.objects.all()
	comp=departments.filter(department_name__startswith='Computer')
	eronics=departments.filter(department_name__startswith='Electronics')
	etrical=departments.filter(department_name__startswith='Electrical')
	bizz=departments.filter(department_name__startswith='Buisness')
	mech=departments.filter(department_name__startswith='Mechanical')
	human=departments.filter(department_name__startswith='Humanities')
	comp_url=comp[0].department_image.url
	event_list=Latest_Event.objects.all()



	return render(request,'AdminStuff/home.html',{'notice_list1':notice_list1,'notice_list2':notice_list2,'comp_url':comp_url,'eronics[0]':eronics,'etrical[0]':etrical,'bizz[0]':bizz,'event_list':event_list})
	
def pdfview(request):
	response =HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment; filename="somefile.pdf"'
	p=canvas.Canvas(response)
	p.drawString(100,100,"Hello World")
	p.showpage()
	p.save()
	return response
def pdf(request):
	file_data=open("CollegeStuff/CollegeWebsite/media/AdminStuff/notice_uploads/files/AdminStuff/notice_uploads/files/github-git-cheat-sheet_ztSFeaO.pdf","rb").read()
	return HttpResponse(file_data,mimetype="application/pdf")


