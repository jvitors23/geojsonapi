from django.contrib.gis.db import models


class ServiceArea(models.Model):
    """Model for service area objects"""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    polygon = models.PolygonField(srid=4326)
    provider = models.ForeignKey("providers.Provider", on_delete=models.CASCADE)
