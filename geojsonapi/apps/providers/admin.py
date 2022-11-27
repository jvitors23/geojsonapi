from django.contrib import admin

from geojsonapi.apps.providers.models import Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):

    list_display = ("name", "owner", "email", "language", "currency")
    ordering = ("name", "id")
    readonly_fields = ("created_at", "modified_at")
