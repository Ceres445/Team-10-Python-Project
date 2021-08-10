from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from home.models import Classes


class Assignment(models.Model):
    key_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    title = models.TextField(max_length=400, default="Title")
    questions = models.FileField(blank=True, upload_to='questions/')
    created_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.key_class.class_name} - {self.title}"


class Upload(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads', null=False)

    def __str__(self):
        return f"{self.author.username} - {self.assignment}"
