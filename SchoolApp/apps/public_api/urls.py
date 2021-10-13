from django.conf.urls import url
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="Edu Orange Documentation",
      default_version='v1',
      description="API documentation for the website, generated by Redoc",
      contact=openapi.Contact(email="https://github.com/Ceres445/Team-10-Python-Project/issues"),
      license=openapi.License(name="MIT License",
                              url='https://github.com/Ceres445/Team-10-Python-Project/blob/master/LICENSE'),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('assignments/', views.AssignmentList.as_view()),
    path('uploads/', views.UploadList.as_view()),
    path('uploads/<int:pk>', views.UploadDetail.as_view()),
    path('time_table/', views.TimeTableList.as_view()),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='docs'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
