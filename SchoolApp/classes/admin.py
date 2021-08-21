from django.contrib import admin

from .models import Assignment, Upload, ClassInvitation

# Register your models here.
admin.site.register(Assignment)
admin.site.register(Upload)
admin.site.register(ClassInvitation)
