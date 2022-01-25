from rest_framework import serializers

from apps.classes.models import Assignment, Upload
from apps.home.models import Classes
from apps.timetable.models import ClassTime
from .models import Post, Comment, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=False
    )

    class Meta:
        model = Post
        depth = 1
        fields = (
            "id",
            "title",
            "content",
            "author",
            "created_at",
            "comments",
            "category",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "body", "author", "post", "created_at"]


class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    key_class = serializers.SlugRelatedField(
        many=False,
        required=False,
        queryset=Classes.objects.all(),
        slug_field="class_name",
        allow_null=True,
    )

    class Meta:
        model = Category
        fields = ["id", "name", "posts", "key_class"]


class AssignmentSerializer(serializers.ModelSerializer):
    upload = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = ["id", "title", "key_class", "upload"]


class UploadSerializer(serializers.ModelSerializer):
    assignment = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Upload
        fields = ["id", "author", "file", "assignment"]


class TimeTableSerializer(serializers.ModelSerializer):
    key_class = serializers.SlugRelatedField(
        many=False,
        required=False,
        queryset=Classes.objects.all(),
        slug_field="class_name",
        allow_null=True,
    )

    class Meta:
        model = ClassTime
        fields = ["pk", "key_class", "subject", "day", "time", "link"]
