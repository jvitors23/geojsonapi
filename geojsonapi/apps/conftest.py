import pytest
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Polygon
from rest_framework.test import APIClient

from geojsonapi.apps.providers.models import Provider
from geojsonapi.apps.serviceareas.models import ServiceArea

User = get_user_model()


@pytest.fixture(scope="function")
def user() -> User:
    return User.objects.create_user(email="test@email.com", password="test1234", name="teste 123")


@pytest.fixture(scope="function")
def provider(user: User) -> Provider:
    return Provider.objects.create(
        owner=user,
        language="pt",
        currency="BRL",
        email="testprovider@email.com",
        name="test_provider",
        phone_number="5512345678",
    )


@pytest.fixture(scope="function")
def service_area(provider: Provider) -> ServiceArea:
    return ServiceArea.objects.create(
        provider=provider,
        price=250.0,
        name="test_service_area",
        polygon=Polygon(((3, 3), (0, 1), (1, 1), (1, 0), (3, 3))),
    )


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture(scope="function")
def authenticated_api_client(api_client: APIClient, user: User) -> APIClient:
    api_client.force_authenticate(user=user)
    return api_client
