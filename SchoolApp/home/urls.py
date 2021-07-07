from django.urls import include, path

import home.views as views

urlpatterns = [
    path('', views.index, name="home_page"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("profile/edit", views.edit_profile, name="edit_profile"),
    path("profile/", views.view_profile, name="profile"),
    path('avatar_change/', views.change_avatar, name="change_avatar"),
    path('post/<int:pk>/', views.view_post, name="post")
]
