from django.shortcuts import render

from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer, BlogPostTransformSerializer
# Create your views here.


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostTransformSerializer
    look_up_field = "pk"
