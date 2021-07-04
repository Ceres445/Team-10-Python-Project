from django.conf.urls import url
from django.urls import include

import home.views as views

urlpatterns = [
    url(r'^$', views.index, name="home_page"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", views.register, name="register"),
    url("^profile/edit", views.edit_profile, name="edit_profile"),
    url("^profile/", views.view_profile, name="profile"),
    url('^avatar_change/', views.change_avatar, name="change_avatar"),
]
