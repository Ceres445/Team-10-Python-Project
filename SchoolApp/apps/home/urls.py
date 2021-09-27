from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView

from apps.home import views
from apps.home.map import PostSitemap, StaticSitemap

sitemaps = {
    'blog': PostSitemap,
    'static': StaticSitemap
}
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
    path("robots.txt", TemplateView.as_view(template_name="../../templates/home/templates/home/robots.txt",
                                            content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
