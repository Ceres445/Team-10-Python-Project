from django.urls import path

import classes.views as views

urlpatterns = [
    path('', views.classes_view, name='classesView'),
    path('<int:pk>', views.classes_detail, name='classesDetail'),
    path('assignment/create/<int:pk>', views.assignment_creation, name="assignmentCreate"),
    path('assignment/view/<int:pk>', views.view_submissions, name="assignmentView"),
    path('<int:pk>/submit', views.assignment_submit, name="assignmentSubmit"),
    path('<int:pk>/invite', views.invite_users, name='InviteUser'),
    path('invite/accept/<str:key>', views.accept_invite, name='AcceptInvite')
]
