from django.urls import include, path
from rest_framework.routers import DefaultRouter

from geojsonapi.apps.providers.views import ProviderViewset

app_name = "providers"

router = DefaultRouter()
router.register("", ProviderViewset)

urlpatterns = [
    path("", include(router.urls)),
]
