import pycountry
from django.db import models

from geojsonapi.apps.core.models import BaseModel

LANGUAGE_CHOICES = sorted(
    [(lang.alpha_2, lang.name) for lang in list(pycountry.languages) if hasattr(lang, "alpha_2")], key=lambda x: x[1]
)
CURRENCY_CHOICES = sorted(
    [(cur.alpha_3, f"{cur.alpha_3} - {cur.name}") for cur in list(pycountry.currencies) if hasattr(cur, "alpha_3")],
    key=lambda x: x[1],
)


class Provider(BaseModel):
    """Provider model."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
