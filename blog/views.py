from rest_framework import viewsets
from rest_framework.response import Response

from blog.models import Blog, Comment
from blog.serializers import BlogSerializer, CommentSerializer

class BlogViewset(viewsets.ModelViewSet):
    """Blog Viewset"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request):
        blogs = Blog.objects.all()
        return Response({'blogs': blogs}, template_name='blog/blog.html')

class CommentViewset(viewsets.ModelViewSet):
    """Comment Viewset"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
