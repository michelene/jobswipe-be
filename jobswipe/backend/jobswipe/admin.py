from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Job, NewJobList


admin.site.register(User, UserAdmin)
admin.site.register(Job)
admin.site.register(NewJobList)
