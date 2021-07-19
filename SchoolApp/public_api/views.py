from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from . import serializers
from .models import Post, Comment, Category
from .permissions import IsAuthorOrReadOnly, IsInClass


def get_queryset(user, model, category_param=None, user_param=None, **kwargs):
    if user.is_staff:
        queryset = model.objects.all()  # return all objects
    elif user.is_authenticated:
        # include all categories except class
        queryset = model.objects.all().exclude(**{kwargs.get('name'): 'Class'}) | \
                   model.objects.all().filter(
                       **{kwargs.get('class_in'): user.profile.courses.all(),  # include classes in which user is in
                          kwargs.get('name'): 'Class'})  # return class objects for user
    else:
        queryset = model.objects.all().exclude(**{kwargs.get('name'): 'Class'})  # block class objects
    if model is not Category:
        if category_param in ['Class', 'Public', 'Forum', 'Site']:
            # print([(x.category.name == category, list(x.category.name)) for x in queryset], list(category))
            queryset = queryset.filter(
                **{kwargs.get('name'): category_param.strip("'")})  # filter against given category
            # print(queryset)
            if category_param == 'Class':
                if user.is_authenticated:
                    if not user.is_staff:
                        queryset = queryset.filter(**{kwargs.get('class_in'): user.profile.courses.all()})
                else:
                    raise PermissionDenied("Non authenticated users cannot see classes")
        elif category_param is not None:
            raise Http404
    if user_param is not None:
        get_object_or_404(User, username=user_param)  # raise error if author not found
        # print('filtering', user)
        queryset = queryset.filter(author__username=user_param)
    return queryset


class PostList(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        category_param = self.request.query_params.get('category')
        user_param = self.request.query_params.get('author')
        queryset = get_queryset(self.request.user, Post, category_param, user_param, name='category__name',
                                class_in='category__key_class__in')
        class_param = self.request.query_params.get('class')
        if category_param == 'Class' and class_param is not None:
            queryset = queryset.filter(category__key_class__class_name=class_param)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # TODO: block users from creating posts in wrong categories


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsInClass]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user_param = self.request.query_params.get('author')
        queryset = get_queryset(self.request.user, Comment, None, user_param,
                                class_in='post__category__key_class__in',
                                name='post__category__name')
        post = self.request.query_params.get('post', '')
        if post != '':
            queryset = queryset.filter(post__id=post.strip("'"))
            # post = get_object_or_404(Post, id=post.strip("'"))
            try:
                post = Post.objects.get(id=post.strip("'"))
            except ObjectDoesNotExist:
                return queryset
            else:
                if post.category.name == 'Class':
                    if self.request.user.is_authenticated:
                        if not self.request.user.is_staff:
                            queryset = queryset.filter(
                                post__category__key_class__in=self.request.user.profile.courses.all()
                            )
                    else:
                        raise PermissionDenied("Non authenticated users cannot see classes")
        return queryset


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly, IsInClass]


class CategoryList(generics.ListAPIView):
    def get_queryset(self):
        queryset = get_queryset(self.request.user, Category, class_in='key_class__in', name='name')
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        class_param = self.request.query_params.get('class')
        if name == 'Class' and class_param is not None:
            queryset = queryset.filter(key_class__class_name=class_param)
        return queryset

    serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # only admin users can create new categories manually
