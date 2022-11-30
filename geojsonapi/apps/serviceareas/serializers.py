from decimal import Decimal
from typing import Dict

from django.contrib.gis.geos import Polygon
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from geojsonapi.apps.providers.models import Provider
from geojsonapi.apps.serviceareas.models import ServiceArea


class CoordinateSerializer(serializers.Serializer):
    lat = serializers.DecimalField(coerce_to_string=False, required=True, max_digits=10, decimal_places=5)
    lng = serializers.DecimalField(coerce_to_string=False, required=True, max_digits=10, decimal_places=5)


class ServiceAreaProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ("name", "id")
        read_only_fields = ("id", "name")


class ServiceAreaSerializer(serializers.ModelSerializer):
    """Serializer for Service Area objects"""

    price = serializers.DecimalField(coerce_to_string=False, max_digits=10, decimal_places=2, min_value=Decimal("0.0"))

    class Meta:
        model = ServiceArea
        fields = ("id", "name", "price", "polygon", "provider")
        read_only_fields = ("id",)

    def to_representation(self, instance):
        self.fields["provider"] = ServiceAreaProviderSerializer(read_only=True)
        return super().to_representation(instance)

    def validate(self, data: Dict) -> Dict:
        coordinates = data.get("polygon")
        try:
            if coordinates:
                CoordinateSerializer(data=coordinates, many=True).is_valid(raise_exception=True)
                Polygon([(float(i["lat"]), float(i["lng"])) for i in coordinates])
        except Exception:
            raise ValidationError({"polygon": _("Invalid coordinates.")})
        return data

    def create(self, validated_data: Dict) -> ServiceArea:
        """Create a service area"""
        polygon = Polygon([(float(i["lat"]), float(i["lng"])) for i in validated_data.pop("polygon")])
        return ServiceArea.objects.create(polygon=polygon, **validated_data)

    def update(self, instance: ServiceArea, validated_data: Dict) -> ServiceArea:
        """Update a service area"""
        polygon = validated_data.get("polygon")
        if polygon:
            validated_data["polygon"] = Polygon([(float(i["lat"]), float(i["lng"])) for i in polygon])
        return super().update(instance, validated_data)
