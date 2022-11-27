from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api/(?P<version>(v1))/users", include("geojsonapi.apps.users.urls")),
]
