from django.contrib import admin

# Register your models here.
from apps.public_api.models import Post, Comment, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
