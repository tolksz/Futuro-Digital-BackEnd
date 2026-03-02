from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from .base_model import BaseModel
from .reporter import Reporter
from .magazine import Magazine
from django.utils.translation import gettext_lazy as _
from datetime import date


class Article(BaseModel):
    title = models.CharField(max_length=100,
                             verbose_name="Title",
                             help_text=_("Insira o título da reportagem"))
    pub_date = models.DateField(verbose_name=_("Published in"))
    reporter = models.ForeignKey(Reporter, on_delete=models.RESTRICT,)
    magazines = models.ManyToManyField(Magazine)

    def __str__(self):
        return f"{self.title} by {self.reporter.name if self.reporter is not None else 'Anônimo'}"

    def clean(self):
        today = date.today()
        if self.pub_date < today:
            raise ValidationError({"pub_date": _("Published date must be"
                                                 " today or after.")},
                                  code="error1"
                                  )