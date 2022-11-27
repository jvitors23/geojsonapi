from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Base model class."""

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs) -> None:
        """Override saving object."""

        if self.pk:
            self.modified_at = timezone.now()

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
