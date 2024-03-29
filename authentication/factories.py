import factory
from factory.django import DjangoModelFactory

from authentication.models import User


class UserFactory(DjangoModelFactory):
    """User factory."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall("set_password", "defaultpassword")
