from typing import Dict

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
class TestUserPublicApi:
    """Test the user API (public)"""

    CREATE_USER_URL = reverse_lazy("users:create", kwargs={"version": "v1"})
    ME_URL = reverse_lazy("users:manage-user", kwargs={"version": "v1"})
    TOKEN_URL = reverse_lazy("users:token", kwargs={"version": "v1"})

    def test_create_valid_user_success(self, api_client: APIClient) -> None:
        """Test creating user with valid payload is successful"""
        payload = {"email": "test@jvss.com", "name": "jose", "password": "test123"}
        response = api_client.post(self.CREATE_USER_URL, payload)
        user = User.objects.get(**response.data)

        assert response.status_code == status.HTTP_201_CREATED
        assert user.check_password(payload["password"])
        assert "password" not in response.data

    @pytest.mark.django_db
    def test_user_exists(self, api_client: APIClient, user: User) -> None:
        """Test creating a user that already exists fails"""
        payload = {"email": user.email, "password": "test123", "name": user.name}

        response = api_client.post(self.CREATE_USER_URL, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_password_is_too_short(self, api_client: APIClient) -> None:
        """Test that the password must have more than 5 characters"""
        payload = {"email": "jvss@email.com", "name": "jose", "password": "pw"}
        response = api_client.post(self.CREATE_USER_URL, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        user_exists = User.objects.filter(email=payload["email"]).exists()

        assert user_exists is False

    def test_create_token_for_user(self, api_client: APIClient, user: User) -> None:
        """Test that a token is created for the user"""
        payload = {
            "email": user.email,
            "password": "test1234",
        }
        response = api_client.post(self.TOKEN_URL, payload)

        assert response.status_code == status.HTTP_200_OK
        assert "token" in response.data

    def test_create_token_invalid_credentials(self, api_client: APIClient, user: User) -> None:
        """Test that token is not created if invalid credentials are given"""

        payload = {"email": user.email, "password": "wrong"}
        response = api_client.post(self.TOKEN_URL, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "token" not in response.data

    def test_create_token_no_user(self, api_client: APIClient) -> None:
        """Test that token is not created if user doesn't exist"""
        payload = {"email": "jv@email.com", "password": "wrong"}
        response = api_client.post(self.TOKEN_URL, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "token" not in response.data

    @pytest.mark.parametrize(
        "payload",
        [
            ({"email": "test@email.com"},),
            ({"email": "test@email.com", "password": None}),
            ({"email": "test@email.com", "password": ""}),
            ({"email": "", "password": "1234455"}),
            ({"email": None, "password": "1234455"}),
            ({"password": "1234455"}),
        ],
    )
    def test_create_token_missing_field(self, api_client: APIClient, user: User, payload: Dict) -> None:
        """Test that email and password are required"""
        response = api_client.post(self.TOKEN_URL, payload=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "token" not in response.data

    def test_retrieve_user_unauthorized(self, api_client: APIClient) -> None:
        """Test that authentication is required for users"""
        response = api_client.get(self.ME_URL)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
