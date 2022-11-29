from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from geojsonapi.apps.providers.models import Provider
from geojsonapi.apps.providers.permissions import OwnProviderPermission
from geojsonapi.apps.providers.serializers import ProviderSerializer


class ProviderViewset(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [IsAuthenticated, OwnProviderPermission]
