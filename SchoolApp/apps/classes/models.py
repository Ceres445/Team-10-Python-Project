from datetime import timedelta

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from invitations.adapters import get_invitations_adapter
from invitations.base_invitation import AbstractBaseInvitation

from apps.home.models import Classes


class Assignment(models.Model):
    key_class = models.ForeignKey(
        Classes, on_delete=models.CASCADE, related_name="assignments"
    )
    title = models.TextField(max_length=400, default="Title")
    questions = models.FileField(blank=True, upload_to="questions/")
    created_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(blank=True, null=True)

    def is_active(self):
        if self.ends_at is None:
            if self.created_at < (timezone.now() - timedelta(days=120)):
                return False
            return True
        if self.ends_at > timezone.now():
            return True
        return False

    def __str__(self):
        return f"{self.key_class.class_name} - {self.title}"


class Upload(models.Model):
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name="upload"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploads")
    file = models.FileField(upload_to="uploads", null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.assignment}"


class ClassInvitation(AbstractBaseInvitation):
    email = models.EmailField(
        unique=False, verbose_name="email_address", max_length=420
    )
    created = models.DateTimeField(verbose_name="created", default=timezone.now)
    invited_class = models.ForeignKey(
        Classes, on_delete=models.CASCADE, related_name="invitees"
    )

    @classmethod
    def create(cls, email, inviter=None, **kwargs):
        key = get_random_string(64).lower()
        instance = cls._default_manager.create(
            email=email,
            invited_class=kwargs.pop("invited_class", None),
            key=key,
            inviter=inviter,
            **kwargs,
        )
        return instance

    def key_expired(self):
        expiration_date = self.sent + timedelta(days=3)
        return expiration_date <= timezone.now()

    def send_invitation(self, request, **kwargs):
        invite_url = reverse("AcceptInvite", args=[self.key])
        ctx = kwargs
        ctx.update(
            {
                "invite_url": request.build_absolute_uri(invite_url),
                "register_url": request.build_absolute_uri(reverse("register")),
                "site_name": self.invited_class.class_name,
                "email": self.email,
                "key": self.key,
                "inviter": self.inviter,
            }
        )

        email_template = "emails/email_invite"

        get_invitations_adapter().send_mail(email_template, self.email, ctx)
        self.sent = timezone.now()
        self.save()

    def __str__(self):
        return "Invite: {0}".format(self.email)
