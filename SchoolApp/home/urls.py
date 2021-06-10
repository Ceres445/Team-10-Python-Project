from django.conf.urls import url
from django.urls import include

import home.views as views

urlpatterns = [
    url("", views.index, name="index")
]
