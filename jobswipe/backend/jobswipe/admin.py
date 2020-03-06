from django.contrib import admin
from .models import Job, JobList, JobSeeker

# Register your models here.

admin.site.register(Job)
admin.site.register(JobList)
admin.site.register(JobSeeker)
