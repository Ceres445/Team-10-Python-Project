from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from rest_framework import generics, permissions

from . import serializers
from .models import Post, Comment, Category
from .permissions import IsAuthorOrReadOnly, IsInClass


def get_queryset(user, model, **kwargs):
    if user.is_staff:
        queryset = model.objects.all()  # return all objects
    elif user.is_authenticated:
        queryset = model.objects.all().exclude(
            **{kwargs.pop('class_in'): user.profile.courses.all()})  # return class objects for user
    else:
        queryset = model.objects.all().exclude(**{kwargs.pop('name'): 'Class'})  # block class objects
    return queryset


class PostList(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        queryset = get_queryset(self.request.user, Post, name='category__name',
                                class_in='category__key_class__in')
        category = self.request.query_params.get('category', '')
        if category in ['Class', 'Public', 'Forum', 'Site']:
            queryset = Post.objects.all()
            # print([(x.category.name == category, list(x.category.name)) for x in queryset], list(category))
            queryset = queryset.filter(category__name=category.strip("'"))  # filter against given category
            # print(queryset)
            if category == 'Class':
                if self.request.user.is_authenticated:
                    if not self.request.user.is_staff:
                        queryset = queryset.filter(category__key_class__in=self.request.user.profile.courses.all())
                else:
                    raise PermissionDenied("Non authenticated users cannot see classes")
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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
        queryset = get_queryset(self.request.user, Comment, class_in='post__category__key_class__in',
                                name='post__category__name')
        post = self.request.query_params.get('post', '')
        if post != '':
            queryset = Comment.objects.all().filter(post__id=post.strip("'"))
            try:
                post = Post.objects.get(id=post.strip("'"))
            except ObjectDoesNotExist:
                return queryset
            else:
                if post.category.name == 'Class':
                    if self.request.user.is_authenticated:
                        if not self.request.user.is_staff:
                            # print('filtering query')
                            # print(queryset)
                            # print(self.request.user.profile.courses.all())
                            # print(queryset[0].post.category.key_class)
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
        return get_queryset(self.request.user, Category, class_in='key_class__in', name='name')

    serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # only admin users can create new categories manually
