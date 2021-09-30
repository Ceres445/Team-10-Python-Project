from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('assignments/', views.AssignmentList.as_view()),
    # path('assignments/', views.AssignmentList.as_view()),
    path('uploads/', views.UploadList.as_view()),
    path('uploads/<int:pk>', views.UploadDetail.as_view()),
    path('time_table/', views.TimeTableList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)