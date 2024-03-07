from django.urls import path
from blog.views import BlogViewset, BlogDetailViewset, BlogSearchViewset

urlpatterns = [
    path("home", BlogViewset.as_view(), name="home"),
    path("blogs", BlogDetailViewset.as_view(), name="blog-detail"),
    path("search", BlogSearchViewset.as_view(), name="blog-search"),
]
