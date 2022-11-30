from django.urls import include, path
from rest_framework.routers import DefaultRouter

from geojsonapi.apps.serviceareas.views import ServiceAreaViewset

app_name = "serviceareas"

router = DefaultRouter()
router.register("", ServiceAreaViewset)

urlpatterns = [
    path("", include(router.urls)),
]
