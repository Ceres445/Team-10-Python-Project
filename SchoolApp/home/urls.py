from django.conf.urls import url
from django.urls import include

import home.views as views

urlpatterns = [
    url(r'^$', views.index, name="home_page"),  # base url "/"
    url(r"^accounts/", include("django.contrib.auth.urls")),  # all stuff related to account
    url(r"^register/", views.register, name="register")  # registering user
]
