from django.urls import include, path
from django.views.generic import TemplateView

import home.views as views

urlpatterns = [
    path('', views.index, name="homePage"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("profile/edit", views.edit_profile, name="editProfile"),
    path("profile/", views.view_profile, name="profile"),
    path("profile/posts", views.view_user_posts, name='viewPosts'),
    path("profile/<str:username>", views.view_profile, name="profileView"),
    path('avatar_change/', views.change_avatar, name="changeAvatar"),
    path('posts', views.view_posts, name="postView"),
    path('posts/<int:pk>/', views.view_post_detail, name="postDetail"),
    path("robots.txt", TemplateView.as_view(template_name="home/robots.txt", content_type="text/plain")),
]
