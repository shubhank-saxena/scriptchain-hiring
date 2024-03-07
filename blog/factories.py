import factory
from factory.django import DjangoModelFactory

from blog.models import Blog, Comment, BlogAuthor

from django.contrib.auth import get_user_model

from faker import Faker

fake = Faker()

class BlogAuthorFactory(DjangoModelFactory):
    class Meta:
        model = BlogAuthor
    
    name = factory.Faker("name")
    bio = factory.Faker("text")

    @factory.post_generation
    def subscribers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # Add provided subscribers
            for subscriber in extracted:
                self.subscribers.add(subscriber)
        else:
            # Create and add a new subscriber if none were provided
            User = get_user_model()
            user = User.objects.create_user(username=fake.user_name(), password='password')            
            self.subscribers.add(user)

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
    author = factory.SubFactory("authentication.factories.UserFactory")
    blog = factory.SubFactory(BlogFactory)
