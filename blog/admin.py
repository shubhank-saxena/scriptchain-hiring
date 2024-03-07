from django.contrib import admin

from blog.models import Blog, BlogAuthor, Comment

admin.site.register(Blog)
admin.site.register(BlogAuthor)
admin.site.register(Comment)
