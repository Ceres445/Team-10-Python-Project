from django.urls import path

import timetable.views as views

urlpatterns = [
    path('', views.view_timetable, name='TimeTable')
]
