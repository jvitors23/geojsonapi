from typing import Dict

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient

from geojsonapi.apps.providers.models import Provider
from geojsonapi.apps.providers.serializers import ProviderSerializer

User = get_user_model()


@pytest.mark.django_db
class TestProvidersAPI:
    """Tests for the providers API."""

    PROVIDERS_URL = reverse_lazy("providers:provider-list")

    def test_auth_required(self, api_client: APIClient) -> None:
        """Test that authentication is required"""
        response = api_client.get(self.PROVIDERS_URL)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_creating_valid_provider_is_success(self, authenticated_api_client: APIClient, user: User) -> None:
        """Test that creating a provider with valid payload works"""
        payload = {
            "name": "test123",
            "email": "teste@email.com",
            "phone_number": "7512345678",
            "language": "en",
            "currency": "USD",
        }
        response = authenticated_api_client.post(self.PROVIDERS_URL, payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert Provider.objects.filter(email=payload["email"]).exists()

    @pytest.mark.parametrize(
        "invalid_payload",
        [
            (
                {
                    "name": "",
                    "email": "teste@email.com",
                    "phone_number": "7512345678",
                    "language": "en",
                    "currency": "USD",
                }
            ),
            (
                {
                    "name": "test123",
                    "email": "teste@email.com",
                    "phone_number": "7512345678",
                    "language": "en",
                    "currency": "invalid currency",
                }
            ),
            (
                {
                    "name": "test123",
                    "email": "teste@email.com",
                    "phone_number": "7512345678",
                    "language": "invalid lang",
                    "currency": "USD",
                }
            ),
            (
                {
                    "name": "test123",
                    "email": "invalid email",
                    "phone_number": "7512345678",
                    "language": "en",
                    "currency": "USD",
                }
            ),
        ],
    )
    def test_creating_invalid_provider_payload_fails(
        self, authenticated_api_client: APIClient, user: User, invalid_payload: Dict
    ) -> None:
        """Test that creating a provider with invalid payload fails"""
        response = authenticated_api_client.post(self.PROVIDERS_URL, invalid_payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Provider.objects.all().count() == 0

    def test_user_can_update_his_own_providers(
        self, user: User, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Tests if user can update his own provider"""
        payload = {
            "name": "updating",
            "email": "update@email.com",
            "phone_number": "7512345678",
            "language": "en",
            "currency": "USD",
        }
        url = f"{self.PROVIDERS_URL}{provider.id}/"
        response = authenticated_api_client.put(url, payload)
        assert response.status_code == status.HTTP_200_OK

        provider = Provider.objects.get(email=payload["email"])

        assert provider.email == payload["email"]
        assert provider.name == payload["name"]
        assert provider.phone_number == payload["phone_number"]
        assert provider.language == payload["language"]
        assert provider.currency == payload["currency"]

    def test_user_can_partial_update_his_own_providers(
        self, user: User, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Tests if user can do partial update his own provider"""
        payload = {
            "language": "en",
            "currency": "USD",
        }
        url = f"{self.PROVIDERS_URL}{provider.id}/"
        response = authenticated_api_client.patch(url, payload)
        assert response.status_code == status.HTTP_200_OK

        provider = Provider.objects.get(pk=provider.pk)

        assert provider.language == payload["language"]
        assert provider.currency == payload["currency"]

    def test_user_cant_update_read_only_fields(
        self, user: User, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Tests if user can do partial update his own provider"""
        payload = {
            "id": 122,
        }
        url = f"{self.PROVIDERS_URL}{provider.id}/"
        authenticated_api_client.patch(url, payload)
        old_id = provider.id
        provider.refresh_from_db()
        assert provider.id == old_id

    def test_user_cant_update_other_user_providers(self, authenticated_api_client: APIClient) -> None:
        """Tests if user can't do partial update other user provider"""
        payload = {
            "name": "updating",
            "email": "update@email.com",
            "phone_number": "7512345678",
            "language": "en",
            "currency": "USD",
        }
        other_user = User.objects.create_user(name="other", email="other@email.com", password="pass123")
        provider = Provider.objects.create(
            owner=other_user,
            language="pt",
            currency="BRL",
            email="testother@email.com",
            name="test_provider",
            phone_number="5512345678",
        )
        url = f"{self.PROVIDERS_URL}{provider.id}/"
        response = authenticated_api_client.put(url, payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

        response = authenticated_api_client.patch(url, payload)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_authenticated_user_can_list_providers(
        self, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Test if authenticated user can list providers"""
        response = authenticated_api_client.get(self.PROVIDERS_URL)

        providers = Provider.objects.all().order_by("-id")
        serializer = ProviderSerializer(providers, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_authenticated_user_can_retrieve_provider(
        self, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Test if authenticated user can retrieve provider"""
        url = f"{self.PROVIDERS_URL}{provider.id}/"
        response = authenticated_api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == provider.name
        assert response.data["email"] == provider.email
        assert response.data["phone_number"] == provider.phone_number
        assert response.data["language"] == provider.language
        assert response.data["currency"] == provider.currency

    def test_authenticated_user_can_delete_provider(
        self, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Test if authenticated user can delete provider"""
        url = f"{self.PROVIDERS_URL}{provider.id}/"
        response = authenticated_api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Provider.objects.all().count() == 0

    def test_authenticated_user_cant_delete_other_user_provider(self, authenticated_api_client: APIClient) -> None:
        """Test if authenticated user can't delete other user provider"""
        other_user = User.objects.create_user(name="other", email="other@email.com", password="pass123")
        provider = Provider.objects.create(
            owner=other_user,
            language="pt",
            currency="BRL",
            email="testother@email.com",
            name="test_provider",
            phone_number="5512345678",
        )
        url = f"{self.PROVIDERS_URL}{provider.id}/"
        response = authenticated_api_client.delete(url)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Provider.objects.all().count() == 1
        assert Provider.objects.filter(email=provider.email).exists()

    def test_authenticated_user_cant_create_provider_with_used_email(
        self, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Test if authenticated user can't  create provider with used email"""
        payload = {
            "name": "test123",
            "email": provider.email,
            "phone_number": "7512345678",
            "language": "en",
            "currency": "USD",
        }
        response = authenticated_api_client.post(self.PROVIDERS_URL, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Provider.objects.all().count() == 1
