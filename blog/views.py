from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from django.db.models import Q

from blog.models import Blog, Comment

class BlogViewset(generics.ListAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def list(self, request):
        # # Worst Run
        # queryset = Blog.objects.all()

        # Best Run
        queryset = Blog.objects.select_related('author').all()
        return Response({'blogs': queryset})
    
class BlogDetailViewset(generics.ListAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog_detail.html'

    def list(self, request, *args, **kwargs):
        # # Worst run
        # queryset = Blog.objects.all()

        # # Better run
        # queryset = Blog.objects.select_related('author').all()

        # Best Run
        queryset = Blog.objects.select_related('author').prefetch_related('author__subscribers').all()
        return Response({'blogs': queryset})

class BlogSearchViewset(generics.ListAPIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def list(self, request):
        queryset = Blog.objects.select_related('author').all().filter(Q(title__icontains=request.GET.get('search', '')) | Q(content__icontains=request.GET.get('search', '')))
        return Response({'blogs': queryset})
