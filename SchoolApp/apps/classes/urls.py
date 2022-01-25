from django.urls import path

import apps.classes.views as views

urlpatterns = [
    path("", views.classes_view, name="ClassesView"),
    path("<int:pk>", views.classes_detail, name="ClassesDetail"),
    path("<int:pk>/submit", views.assignment_submit, name="AssignmentSubmit"),
    path("<int:pk>/invite", views.invite_users, name="InviteUser"),
    path("<int:pk>/join", views.join_class, name="JoinClass"),
    path(
        "assignment/create/<int:pk>", views.assignment_creation, name="AssignmentCreate"
    ),
    path("assignment/view/<int:pk>", views.view_submissions, name="AssignmentView"),
    path("invite/accept/<str:key>", views.accept_invite, name="AcceptInvite"),
]
