# from pyexpat import model
from rest_framework import serializers
from .models import Memory, Post_Favorite, Post_Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate





class UserSerializer(serializers.ModelSerializer):
    memories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Memory.objects.all())
    post_favorites = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post_Favorite.objects.all())
    post_comments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post_Comment.objects.all())

    class Meta:
        model = User  # tell django which model to use
        fields = ['id', 'username', 'email', 'password', 'memories',
                  'post_favorites', 'post_comments', ]  # hide password
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password' ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# Login Serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Login Credentials")


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory  # tell django which model to use
        # tell django which fields to include
        fields = ('__all__')


class PostFavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Post_Favorite
        fields = ['user', 'memory', 'id', 'like']


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Post_Comment
        fields = ['user', 'memory', 'id', 'comment']
