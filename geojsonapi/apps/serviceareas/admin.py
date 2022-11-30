from django.contrib import admin

from geojsonapi.apps.serviceareas.models import ServiceArea


@admin.register(ServiceArea)
class ProviderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "price",
        "provider",
    )
    ordering = ("name", "id")
