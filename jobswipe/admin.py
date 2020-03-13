from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Job, Saved
# from .models import User, Job, Saved, Unreviewed


admin.site.register(User, UserAdmin)
admin.site.register(Job)
admin.site.register(Saved)
# admin.site.register(Unreviewed)
