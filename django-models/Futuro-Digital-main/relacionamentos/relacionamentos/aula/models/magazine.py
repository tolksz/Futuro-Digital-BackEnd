from django.core.validators import MinValueValidator

from .base_model import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Magazine(BaseModel):
    name = models.CharField(max_length=100,
                            help_text=_("The name of the Magazine"),
                            verbose_name=_("Magazine Name"))
    edition = models.IntegerField(verbose_name=_("Edition"), unique=True,
                                  validators=[MinValueValidator(1),],
                                  help_text=_("The edition of the Magazine"),)
    def __str__(self):
        return self.name