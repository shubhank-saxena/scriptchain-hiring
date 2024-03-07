from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    password = serializers.CharField(
        write_only=True, min_length=8, max_length=100, required=True
    )
    id = serializers.UUIDField(read_only=True)

    class Meta:
        """Meta class."""

        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "account_created",
            "account_updated",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(UserSerializer):
    """User update serializer."""

    password = serializers.CharField(write_only=True, min_length=8, max_length=100)
    id = serializers.UUIDField(read_only=True)

    class Meta:
        """Meta class."""

        model = User
        fields = [
            "id",
            "password",
            "first_name",
            "last_name",
            "account_created",
            "account_updated",
        ]

    def update(self, instance_obj, validated_data):
        new_password = validated_data.pop("password", None)
        if new_password is not None:
            instance_obj.set_password(new_password)
        for key, value in validated_data.items():
            setattr(instance_obj, key, value)
        instance_obj.save()
        return instance_obj
