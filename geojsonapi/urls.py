from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

API_VERSION = "v1"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-swagger"),
    path(f"api/{API_VERSION}/users/", include("geojsonapi.apps.users.urls")),
    path(f"api/{API_VERSION}/providers/", include("geojsonapi.apps.providers.urls")),
    path(f"api/{API_VERSION}/serviceareas/", include("geojsonapi.apps.serviceareas.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
