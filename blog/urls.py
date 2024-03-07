from django.urls import path
from blog.views import BlogViewset

urlpatterns = [
    path("home", BlogViewset.as_view({"get": "list"})),
]
