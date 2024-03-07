import random

from django.core.management.base import BaseCommand
from django.db import transaction

from authentication.factories import UserFactory
from authentication.models import User
from blog.factories import BlogAuthorFactory, BlogFactory, CommentFactory
from blog.models import Blog, BlogAuthor, Comment


class Command(BaseCommand):
    """Command to generate random data."""

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
