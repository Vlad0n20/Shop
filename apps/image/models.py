from django.db import models
from django.utils.translation import gettext_lazy as _

from abstract.models import BaseModel, WhoDidIt


class Image(BaseModel, WhoDidIt):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    image_url = models.URLField(max_length=255, null=True, blank=True)
    alt_text = models.CharField(max_length=255, null=True, blank=True)
    image_type = models.CharField(max_length=15, null=True, blank=True)
    image_size = models.PositiveIntegerField(null=True, blank=True)
    

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering = ('-created_on',)

    def __str__(self):
        return self.image.name
