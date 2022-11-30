import json
from decimal import Decimal
from typing import Dict, Tuple

import pytest
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point, Polygon
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient

from geojsonapi.apps.providers.models import Provider
from geojsonapi.apps.serviceareas.models import ServiceArea
from geojsonapi.apps.serviceareas.serializers import ServiceAreaSerializer

User = get_user_model()


@pytest.mark.django_db
class TestServiceAreaAPI:
    """Tests for the service area API."""

    SERVICE_AREA_URL = reverse_lazy("serviceareas:servicearea-list")

    @staticmethod
    def get_valid_service_area_payload(provider: Provider):
        return {
            "name": "test123",
            "price": 240.0,
            "provider": provider.id,
            "polygon": [
                {"lat": 1, "lng": 1},
                {"lat": 1, "lng": -1},
                {"lat": -1, "lng": -1},
                {"lat": -1, "lng": 1},
                {"lat": 1, "lng": 1},
            ],
        }

    def test_auth_required(self, api_client: APIClient) -> None:
        """Test that authentication is required"""
        response = api_client.get(self.SERVICE_AREA_URL)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_creating_valid_service_area_is_success(
        self, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Test that creating a service area with valid payload works"""
        payload = self.get_valid_service_area_payload(provider)
        response = authenticated_api_client.post(
            self.SERVICE_AREA_URL, json.dumps(payload), content_type="application/json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert ServiceArea.objects.filter(name=payload["name"]).exists()

    @pytest.mark.parametrize(
        "invalid_payload",
        [
            (
                {
                    "name": "test123",
                    "polygon": [
                        {"lat": 1, "lng": 1},
                        {"lat": 1, "lng": -1},
                        {"lat": -1, "lng": -1},
                        {"lat": -1, "lng": 1},
                        {"lat": 1, "lng": 1},
                    ],
                }
            ),
            (
                {
                    "price": 240.0,
                    "polygon": [
                        {"lat": 1, "lng": 1},
                        {"lat": 1, "lng": -1},
                        {"lat": -1, "lng": -1},
                        {"lat": -1, "lng": 1},
                        {"lat": 1, "lng": 1},
                    ],
                }
            ),
            (
                {
                    "name": "test123",
                    "price": 240.0,
                }
            ),
            (
                {
                    "name": "test123",
                    "price": -132,
                    "polygon": [
                        {"lat": 1, "lng": 1},
                        {"lat": 1, "lng": -1},
                        {"lat": -1, "lng": -1},
                        {"lat": -1, "lng": 1},
                        {"lat": 1, "lng": 1},
                    ],
                }
            ),
            (
                {
                    "name": "",
                    "price": 132,
                    "polygon": [
                        {"lat": 1, "lng": 1},
                        {"lat": 1, "lng": -1},
                        {"lat": -1, "lng": -1},
                        {"lat": -1, "lng": 1},
                        {"lat": 1, "lng": 1},
                    ],
                }
            ),
            (
                {
                    "name": "test123",
                    "price": 132,
                    "polygon": None,
                }
            ),
            (
                {
                    "name": "test123",
                    "price": 132,
                    "polygon": [
                        {"last": 1, "lng": 1},
                        {"lat": 1, "lndg": -1},
                        {"lat": -1, "lndg": -1},
                        {"lat": -1, "lndg": 1},
                        {"lat": 1, "ldng": 1},
                    ],
                }
            ),
            (
                {
                    "name": "test123",
                    "price": 132,
                    "polygon": [{"lat": 1, "lng": 1}],
                }
            ),
            (
                {
                    "name": "test123",
                    "price": 132,
                    "polygon": [
                        {"lat": 1, "lng": 1},
                        {"lat": 1, "lng": -1},
                        {"lat": -1, "lng": -1},
                        {"lat": -1, "lng": 1},
                    ],
                }
            ),
        ],
    )
    def test_creating_invalid_provider_payload_fails(
        self, authenticated_api_client: APIClient, provider: Provider, invalid_payload: Dict
    ) -> None:
        """Test that creating a service area with invalid payload fails"""
        invalid_payload["provider"] = provider.id
        response = authenticated_api_client.post(
            self.SERVICE_AREA_URL, json.dumps(invalid_payload), content_type="application/json"
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert ServiceArea.objects.all().count() == 0

    def test_user_cant_create_service_area_for_other_user_providers(
        self, user: User, authenticated_api_client: APIClient, provider: Provider
    ) -> None:
        """Tests if user can't create a service area for other user provider"""
        other_user = User.objects.create_user(name="other", email="other@email.com", password="pass123")
        provider = Provider.objects.create(
            owner=other_user,
            language="pt",
            currency="BRL",
            email="testother@email.com",
            name="test_provider",
            phone_number="5512345678",
        )
        payload = self.get_valid_service_area_payload(provider)

        response = authenticated_api_client.post(
            self.SERVICE_AREA_URL, json.dumps(payload), content_type="application/json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert ServiceArea.objects.count() == 0

    def test_user_can_update_his_own_providers_service_areas(
        self, user: User, authenticated_api_client: APIClient, service_area: ServiceArea
    ) -> None:
        """Tests if user can do update on his own provider's service areas"""
        payload = {
            "name": "update",
            "price": 234.2,
            "provider": service_area.provider_id,
            "polygon": [
                {"lat": 2, "lng": 2},
                {"lat": 1, "lng": -1},
                {"lat": -1, "lng": -1},
                {"lat": -1, "lng": 1},
                {"lat": 2, "lng": 2},
            ],
        }
        url = f"{self.SERVICE_AREA_URL}{service_area.id}/"
        response = authenticated_api_client.put(url, json.dumps(payload), content_type="application/json")
        assert response.status_code == status.HTTP_200_OK
        service_area.refresh_from_db()
        assert service_area.name == payload["name"]
        assert service_area.price == Decimal(str(payload["price"]))
        assert (
            service_area.polygon.coords
            == Polygon([(float(i["lat"]), float(i["lng"])) for i in payload["polygon"]]).coords
        )

    def test_user_can_partial_update_his_own_providers_service_areas(
        self, user: User, authenticated_api_client: APIClient, service_area: ServiceArea
    ) -> None:
        """Tests if user can do partial update on his own provider's service areas"""
        payload = {
            "name": "update",
            "price": 234.2,
        }
        url = f"{self.SERVICE_AREA_URL}{service_area.id}/"
        response = authenticated_api_client.patch(url, json.dumps(payload), content_type="application/json")
        assert response.status_code == status.HTTP_200_OK

        service_area.refresh_from_db()

        assert service_area.name == payload["name"]
        assert service_area.price == Decimal(str(payload["price"]))

    def test_user_cant_update_service_areas_of_not_owned_provider(
        self, authenticated_api_client: APIClient, provider: Provider, service_area: ServiceArea
    ) -> None:
        """Tests if user can't do update other user provider"""
        other_user = User.objects.create_user(name="other", email="other@email.com", password="pass123")
        other_user_provider = Provider.objects.create(
            owner=other_user,
            language="pt",
            currency="BRL",
            email="testother@email.com",
            name="test_provider",
            phone_number="5512345678",
        )
        service_area.provider = other_user_provider
        service_area.save()
        payload = self.get_valid_service_area_payload(provider)

        url = f"{self.SERVICE_AREA_URL}{service_area.id}/"
        response = authenticated_api_client.put(url, json.dumps(payload), content_type="application/json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

        response = authenticated_api_client.patch(url, json.dumps(payload), content_type="application/json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_authenticated_user_can_list_service_areas(
        self, authenticated_api_client: APIClient, service_area: ServiceArea
    ) -> None:
        """Test if authenticated user can list service areas"""
        response = authenticated_api_client.get(self.SERVICE_AREA_URL)

        service_areas = ServiceArea.objects.all().order_by("-id")
        serializer = ServiceAreaSerializer(service_areas, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    @pytest.mark.parametrize(
        "coords,number_of_service_areas",
        [
            ((3.5, 3.5), 0),
            ((2.5, 2.5), 1),
            ((1.5, 1.5), 2),
            ((0.5, 0.5), 3),
            ((0, 0), 3),
        ],
    )
    def test_authenticated_user_can_filter_service_areas_by_lat_and_lng_query_params(
        self,
        authenticated_api_client: APIClient,
        provider: Provider,
        coords: Tuple[int, int],
        number_of_service_areas: int,
    ) -> None:
        """Test if authenticated user can filter service areas using lat and lng query params"""
        polygons = [
            Polygon(((1, 1), (1, -1), (-1, -1), (-1, 1), (1, 1))),
            Polygon(((2, 2), (2, -2), (-2, -2), (-2, 2), (2, 2))),
            Polygon(((3, 3), (3, -3), (-3, -3), (-3, 3), (3, 3))),
        ]

        for polygon in polygons:
            ServiceArea.objects.create(name=f"testarea{polygon}", price=20.5, provider=provider, polygon=polygon)

        response = authenticated_api_client.get(self.SERVICE_AREA_URL, {"lat": coords[0], "lng": coords[1]})

        point = Point(coords[0], coords[1])
        service_areas = ServiceArea.objects.filter(polygon__contains=point).all()
        serializer = ServiceAreaSerializer(service_areas, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_authenticated_user_can_retrieve_service_area(
        self, authenticated_api_client: APIClient, service_area: ServiceArea
    ) -> None:
        """Test if authenticated user can retrieve service area"""
        url = f"{self.SERVICE_AREA_URL}{service_area.id}/"
        response = authenticated_api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == service_area.name
        assert response.data["price"] == service_area.price

    def test_authenticated_user_can_delete_service_area(
        self, authenticated_api_client: APIClient, service_area: ServiceArea
    ) -> None:
        """Test if authenticated user can delete provider"""
        url = f"{self.SERVICE_AREA_URL}{service_area.id}/"
        response = authenticated_api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert ServiceArea.objects.all().count() == 0

    def test_authenticated_user_cant_delete_other_user_provider_service_area(
        self, authenticated_api_client: APIClient, provider: Provider, service_area: ServiceArea
    ) -> None:
        """Test if authenticated user can't delete other user provider"""
        other_user = User.objects.create_user(name="other", email="other@email.com", password="pass123")
        other_user_provider = Provider.objects.create(
            owner=other_user,
            language="pt",
            currency="BRL",
            email="testother@email.com",
            name="test_provider",
            phone_number="5512345678",
        )
        service_area.provider = other_user_provider
        service_area.save()
        url = f"{self.SERVICE_AREA_URL}{service_area.id}/"
        response = authenticated_api_client.delete(url)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert ServiceArea.objects.all().count() == 1
        assert ServiceArea.objects.filter(name=service_area.name).exists()
