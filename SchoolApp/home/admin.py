from django.contrib import admin

# Register your models here.
from home.models import Profile, Classes

admin.site.register(Profile)
admin.site.register(Classes)