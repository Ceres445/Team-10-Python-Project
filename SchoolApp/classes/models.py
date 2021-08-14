from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from home.models import Classes


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
