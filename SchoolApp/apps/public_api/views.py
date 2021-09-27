from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from rest_framework import generics, permissions

from apps.classes.models import Assignment, Upload
from apps.timetable.models import ClassTime
from .filters import filter_queryset, authenticated_home, anon_home, authenticated_classes, anon, parse_args
from .models import Post, Comment, Category
from .permissions import IsAuthorOrReadOnly, IsInClass
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, \
    AssignmentSerializer, UploadSerializer, \
    TimeTableSerializer


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category_param = self.request.query_params.get('category')
        user_param = self.request.query_params.get('author')
        queryset = filter_queryset(self.request.user, Post, {'authenticated': authenticated_home, 'anon': anon_home},
                                   name='category__name',
                                   class_in='category__key_class__in'
                                   )
        queryset = parse_args(queryset, self.request.user, Post, category_param, user_param, name='category__name',
                              class_in='category__key_class__in')
        class_param = self.request.query_params.get('class')
        if category_param == 'Class' and class_param is not None:
            queryset = queryset.filter(category__key_class__class_name=class_param)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # TODO: block users from creating posts in wrong categories


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsInClass]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user_param = self.request.query_params.get('author')
        queryset = filter_queryset(self.request.user, Comment, {'authenticated': authenticated_home, 'anon': anon_home},
                                   class_in='post__category__key_class__in',
                                   name='post__category__name'
                                   )
        queryset = parse_args(queryset, self.request.user, Comment, None, user_param,
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
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly, IsInClass]


class CategoryList(generics.ListAPIView):
    def get_queryset(self):
        queryset = filter_queryset(self.request.user, Category,
                                   {'authenticated': authenticated_home, 'anon': anon_home},
                                   class_in='key_class__in', name='name'
                                   )
        queryset = parse_args(queryset, self.request.user, Category, class_in='key_class__in', name='name')
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        class_param = self.request.query_params.get('class')
        if name == 'Class' and class_param is not None:
            queryset = queryset.filter(key_class__class_name=class_param)
        return queryset

    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # only admin users can create new categories manually


class AssignmentList(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        return filter_queryset(self.request.user, Assignment,
                               {'authenticated': authenticated_classes,
                                'anon': anon},
                               **{'courses': 'key_class__in', 'teacher': 'key_class__teacher_id'})


class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        return filter_queryset(self.request.user, Assignment,
                               {'authenticated': authenticated_classes,
                                'anon': anon},
                               **{'courses': 'key_class__in', 'teacher': 'key_class__teacher_id'})


class UploadList(generics.ListAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

    def get_queryset(self):
        return filter_queryset(self.request.user, Upload,
                               {'authenticated': authenticated_classes,
                                'anon': anon},
                               **{'courses': 'assignment_key_class__in', 'teacher': 'assignment_key_class__teacher_id'})


class UploadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

    def get_queryset(self):
        return filter_queryset(self.request.user, Upload,
                               {'authenticated': authenticated_classes,
                                'anon': anon},
                               **{'courses': 'assignment_key_class__in', 'teacher': 'assignment_key_class__teacher_id'})


class TimeTableList(generics.ListAPIView):
    queryset = ClassTime.objects.all()
    serializer_class = TimeTableSerializer

    def get_queryset(self):
        return filter_queryset(self.request.user, ClassTime,
                               {'authenticated': authenticated_classes,
                                'anon': anon},
                               **{'courses': 'key_class__in', 'teacher': 'key_class__teacher_id'})
