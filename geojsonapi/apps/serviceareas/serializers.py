from typing import Dict

from django.contrib.gis.geos import Polygon
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from geojsonapi.apps.serviceareas.models import ServiceArea


class CoordinateSerializer(serializers.Serializer):
    lat = serializers.DecimalField(coerce_to_string=False, required=True, max_digits=10, decimal_places=5)
    lng = serializers.DecimalField(coerce_to_string=False, required=True, max_digits=10, decimal_places=5)


class ServiceAreaSerializer(serializers.ModelSerializer):
    """Serializer for Service Area objects"""

    price = serializers.FloatField()

    class Meta:
        model = ServiceArea
        fields = ("id", "name", "price", "provider", "polygon")
        read_only_fields = ("id",)

    def validate(self, data: Dict) -> Dict:
        coordinates = data["polygon"]
        try:
            if coordinates:
                CoordinateSerializer(data=coordinates, many=True).is_valid(raise_exception=True)
                Polygon([(float(i["lat"]), float(i["lng"])) for i in coordinates])
        except Exception:
            raise ValidationError({"polygon": _("Invalid coordinates.")})
        return data

    def create(self, validated_data: Dict) -> ServiceArea:
        polygon = Polygon([(float(i["lat"]), float(i["lng"])) for i in validated_data.pop("polygon")])
        return ServiceArea.objects.create(polygon=polygon, **validated_data)

    def update(self, instance: ServiceArea, validated_data: Dict) -> ServiceArea:
        """Update a service area"""
        polygon = validated_data.pop("polygon")
        if polygon:
            validated_data["polygon"] = Polygon([(float(i["lat"]), float(i["lng"])) for i in polygon])
        return super().update(instance, validated_data)
