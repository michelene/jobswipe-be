from django.contrib import admin
from .models import Job, JobList, Keyword, JobSeeker

# Register your models here.

admin.site.register(Job)
admin.site.register(JobList)
admin.site.register(Keyword)
admin.site.register(JobSeeker)
