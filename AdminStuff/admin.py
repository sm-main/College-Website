from django.contrib import admin
from .models import Notice,News_and_Event,Tenders,File,Department_image,Latest_Event
# Register your models here.
admin.site.register(Notice)
admin.site.register(News_and_Event)
admin.site.register(Tenders)
admin.site.register(File)
admin.site.register(Department_image)
admin.site.register(Latest_Event)