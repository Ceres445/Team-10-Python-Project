from django.contrib import admin

# Register your models here.
from apps.timetable.models import ClassTime, PostAnnouncementDiscord

admin.site.register(ClassTime)
admin.site.register(PostAnnouncementDiscord)
