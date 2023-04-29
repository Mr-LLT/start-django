from django.db import models
from django.utils.translation import gettext_lazy as _


class Abstract(models.Model):
    modtime = models.DateTimeField(_('modtime'), auto_now=True)
    addtime = models.DateTimeField(_('addtime'), auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-addtime',)
