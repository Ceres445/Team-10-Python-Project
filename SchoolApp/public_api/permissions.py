from rest_framework import permissions

from public_api.models import Post


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsInClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not isinstance(obj, Post):
            try:
                obj = obj.post
            except AttributeError:
                raise RuntimeError("Invalid object of type", obj.__type__, 'passed, IsInClass expects Post or Comment')
        if obj.category.name != 'Class':
            return True
        if request.method in permissions.SAFE_METHODS:
            if obj.category.key_class in request.user.profile.courses.all():
                return True
            else:
                return False
        return obj.author == request.user
