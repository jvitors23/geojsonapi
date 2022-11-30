from django.contrib.gis.geos import Point
from django.db.models import QuerySet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from geojsonapi.apps.serviceareas.models import ServiceArea
from geojsonapi.apps.serviceareas.permissions import IsServiceAreaProviderPermission
from geojsonapi.apps.serviceareas.serializers import (
    CoordinateSerializer,
    ServiceAreaSerializer,
)


class ServiceAreaViewset(ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = [IsAuthenticated, IsServiceAreaProviderPermission]

    def __validate_provider(self, serializer) -> None:
        provider = serializer.validated_data.get("provider")
        if provider and provider.owner_id != self.request.user.id:
            raise PermissionDenied()

    def perform_create(self, serializer):
        self.__validate_provider(serializer)
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        self.__validate_provider(serializer)
        return super().perform_create(serializer)

    def get_queryset(self) -> QuerySet:
        """Filter service areas based on lat, lng"""
        if "lat" in self.request.query_params and "lng" in self.request.query_params:
            serializer = CoordinateSerializer(data=self.request.query_params)
            serializer.is_valid(raise_exception=True)
            lng = serializer.validated_data.get("lng")
            lat = serializer.validated_data.get("lat")
            return ServiceArea.objects.filter(polygon__contains=Point((lng, lat), srid=4326))
        return ServiceArea.objects.all()
