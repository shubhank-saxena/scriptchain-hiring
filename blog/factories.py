import factory
from factory.django import DjangoModelFactory

from blog.models import Blog, Comment, BlogAuthor
from authentication.factories import UserFactory

class BlogAuthorFactory(DjangoModelFactory):
    class Meta:
        model = BlogAuthor
    
    name = factory.Faker("company")
    bio = factory.Faker("text")
    created_by = factory.SubFactory(UserFactory)

    # Create subscribers. It is a many to many field
    @factory.post_generation
    def subscribers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # A list of subscribers were passed in, use them
            for subscriber in extracted:
                self.subscribers.add(subscriber)
        else:
            # Add 3 random subscribers.
            for _ in range(3):
                self.subscribers.add(UserFactory())

class BlogFactory(DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.Faker("sentence")
    content = factory.Faker("text")
    author = factory.SubFactory(BlogAuthorFactory)

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Faker("text")
    author = factory.SubFactory(UserFactory)
    blog = factory.SubFactory(BlogFactory)
