from django.db import models
from django.utils.translation import gettext_lazy as _

from abstract.models import BaseModel, WhoDidIt


class Category(BaseModel, WhoDidIt):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey('image.Image', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('-created_on',)
