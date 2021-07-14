from rest_framework import serializers

from home.models import Classes
from .models import Post, Comment, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=False)

    class Meta:
        model = Post
        depth = 1
        fields = ('id', 'title', 'content', 'author', 'created_at', 'comments', 'category')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'author', 'post', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    key_class = serializers.SlugRelatedField(many=False, required=False, queryset=Classes.objects.all(),
                                             slug_field='class_name',
                                             allow_null=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'posts', 'key_class']
