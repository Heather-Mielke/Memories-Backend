from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_date') #tell django how to retrieve all the objects from the DB, order by creted_date decending
    serializer_class = PostSerializer #tell django what serializer to use

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer