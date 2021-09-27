from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.home.models import Classes


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40, blank=False, default='Forum')
    key_class = models.ForeignKey(Classes, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + (str(self.key_class) if self.key_class is not None else '')


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=800)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']


# create and save category whenever a new course is registered
@receiver(post_save, sender=Classes)
def create_category(sender, instance, created, **kwargs):
    if created:
        Category.objects.create(key_class=instance, name='Class')


@receiver(post_save, sender=Classes)
def create_category(sender, instance, **kwargs):
    Category.objects.get(key_class=instance).save()
