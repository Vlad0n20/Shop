from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from ..middleware import current_request
from django.dispatch import receiver
from django.db import models

User = get_user_model()


class WhoDidIt(models.Model):
    """ Abstract model to implement fields created_on/created_by and updated_on/updated_by,
        and to keep them filled up automatically.
    """
    created_on = models.DateTimeField(
        verbose_name='when created',
        auto_now_add=True, editable=False,
    )
    created_by = models.ForeignKey(
        verbose_name='who created',
        to=User, null=True, blank=True, editable=False,
        on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)s_created_by',
    )

    updated_on = models.DateTimeField(
        verbose_name='when updated',
        auto_now=True, editable=False,

    )
    updated_by = models.ForeignKey(
        verbose_name='when updated',
        to=User, null=True, blank=True, editable=False,
        on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by',
    )

    class Meta:
        abstract = True


@receiver(pre_save)
def set_who_did_it(sender, instance, **kwargs):
    if isinstance(instance, WhoDidIt):
        request = current_request()
        user = request.user if request else None
        if user and user.is_authenticated:
            if instance.pk is None:
                instance.created_by = user
            instance.updated_by = user
