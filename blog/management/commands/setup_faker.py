import random

from django.db import transaction
from django.core.management.base import BaseCommand

from authentication.models import User
from blog.models import Blog, Comment, BlogAuthor
from authentication.factories import UserFactory
from blog.factories import BlogFactory, CommentFactory, BlogAuthorFactory


class Command(BaseCommand):
    help = "Generates random data"
    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        User.objects.all().delete()
        Blog.objects.all().delete()
        Comment.objects.all().delete()
        BlogAuthor.objects.all().delete()
        self.stdout.write("Creating new data...")

        people = []
        for _ in range(50):
            person = UserFactory()
            people.append(person)

        authors = []
        for _ in range(10):
            author = BlogAuthorFactory.create()
            authors.append(author)

        for _ in range(12):
            author = random.choice(authors)
            blog = BlogFactory(author=author)
            for _ in range(25):
                commentor = random.choice(people)
                CommentFactory(author=commentor, blog=blog)
