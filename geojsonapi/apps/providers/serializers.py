from rest_framework.serializers import ModelSerializer

from geojsonapi.apps.providers.models import Provider


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ("name", "email", "phone_number", "language", "currency", "owner", "id")
        read_only_fields = ("id",)
