from django.shortcuts import render
from rest_framework import generics
from .serializers import MemorySerializer, PostCommentSerializer, PostFavoriteSerializer, UserSerializer, RegisterSerializer, LoginSerializer
from .models import Memory, Post_Comment, Post_Favorite
from rest_framework import permissions
from rest_framework.response import Response
# from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
# from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from memories_api.permissions import IsCreatorOrReadOnly
from knox.models import AuthToken


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })

# Get User API


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class MyMemoryList(generics.ListAPIView):
    serializer_class = MemorySerializer

    def get_queryset(self):
        """
        This view should return a list of all the memories
        for the currently authenticated user.
        """
        user = self.request.user
        return Memory.objects.filter(creator=user.id)


class MemoryList(generics.ListCreateAPIView):
    # tell django how to retrieve all the objects from the DB, order by creted_date decending
    queryset = Memory.objects.all().order_by('-created_date')
    serializer_class = MemorySerializer  # tell django what serializer to use
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memory.objects.all().order_by('-created_date')
    serializer_class = MemorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]


# favorites
class PostFavoriteList(generics.ListCreateAPIView):
    queryset = Post_Favorite.objects.all()
    serializer_class = PostFavoriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostFavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_Favorite.objects.all().order_by('id')
    serializer_class = PostFavoriteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]

# comments


class PostCommentList(generics.ListCreateAPIView):
    queryset = Post_Comment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_Comment.objects.all().order_by('id')
    serializer_class = PostCommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]
