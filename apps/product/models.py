from django.db import models
from django.utils.translation import gettext_lazy as _

from abstract.models import BaseModel, WhoDidIt



class Product(BaseModel, WhoDidIt):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    images = models.ManyToManyField('image.Image', related_name='products')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('-created_on',)
