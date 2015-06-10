from django.conf.urls import patterns, include, url ,static
from django.contrib import admin
from django.conf import settings
from DepartmentStuff.views import departmentPage,chairman_message,about_dept
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CollegeWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$','AdminStuff.views.home' ),
    url(r'^(?P<dept_name>[-\w]+)/$','DepartmentStuff.views.departmentPage'),
    url(r'^(?P<dept_name>[-\w]+)/about-dept/$','DepartmentStuff.views.about_dept'),
    url(r'^(?P<dept_name>[-\w]+)/chairman-message/$','DepartmentStuff.views.chairman_message',name='chairman-msg'),
    url(r'^(?P<dept_name>[-\w]+)/faculty/$','DepartmentStuff.views.faculty',name='faculty'),
    url(r'^(?P<dept_name>[-\w]+)/faculty-detail/$','DepartmentStuff.views.faculty_detail',name='faculty-detail'),

)+ static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)