from django.db import models
from django.utils.translation import gettext_lazy as _

from abstract.models import BaseModel, WhoDidIt



class Cart(BaseModel, WhoDidIt):
    customer = models.ForeignKey('user.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('order.OrderItem', related_name='carts')
    
    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
        ordering = ('-created_on',)
