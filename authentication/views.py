from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from authentication.serializers import UserSerializer, UserUpdateSerializer


class UserAuthenticationViewSet(generics.CreateAPIView):
    """User authentication view set."""

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @swagger_auto_schema(
        tags=["public"],
        operation_summary="Create a user",
        parameters=[],
        request_body=UserSerializer,
        responses={201: "User Created", 400: "Bad Request"},
    )
    def post(self, request, *args, **kwargs):
        invalid_fields = set(request.data.keys()) - set(
            ["username", "password", "first_name", "last_name"]
        )
        if invalid_fields:
            return Response(
                {field: ["This is an invalid field."] for field in invalid_fields},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginViewSet(GenericAPIView):
    """User login view set."""

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @swagger_auto_schema(
        tags=["authenticated"],
        operation_summary="Get User Information",
        parameters=[],
        responses={200: "User Logged In", 400: "Bad Request"},
    )
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["authenticated"],
        operation_summary="Update user information",
        request_body=UserSerializer,
        responses={200: "User Updated", 400: "Bad Request"},
    )
    def put(self, request, *args, **kwargs):
        invalid_fields = set(request.data.keys()) - set(
            ["password", "first_name", "last_name"]
        )
        if invalid_fields:
            return Response(
                {field: ["This field cannot be updated."] for field in invalid_fields},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
