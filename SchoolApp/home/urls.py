from django.urls import include, path

import home.views as views

urlpatterns = [
    path('', views.index, name="homePage"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("profile/edit", views.edit_profile, name="editProfile"),
    path("profile/", views.view_profile, name="profile"),
    path("profile/posts", views.view_user_posts, name='viewPosts'),
    path('avatar_change/', views.change_avatar, name="changeAvatar"),
    path('post/<int:pk>/', views.view_post_detail, name="postDetail")
]
