from django.conf.urls import patterns, include, url ,static
from django.contrib import admin
from django.conf import settings
from DepartmentStuff.views import DepartmentPage,chairman_message,about_dept

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CollegeWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$','AdminStuff.views.home' ),
    url(r'^(?P<dept_name>[-\w]+)/$',DepartmentPage.as_view()),
    url(r'^(?P<dept_name>[-\w]+)/about-dept/$','DepartmentStuff.views.about_dept'),
    url(r'^(?P<dept_name>[-\w]+)/chairman-message/$','DepartmentStuff.views.chairman_message',name='chairman-msg'),

)+ static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)