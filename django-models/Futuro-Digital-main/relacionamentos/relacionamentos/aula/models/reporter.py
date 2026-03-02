from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from .base_model import BaseModel
from aula.validators import validate_cpf
from django.utils.translation import gettext_lazy as _
from datetime import date
from aula.managers import ReporterManager


class Reporter(BaseModel):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            verbose_name="Reporter",
                            help_text=_("Reporter Name"))

    cpf = models.CharField(max_length=11,
                           validators=[MinLengthValidator(11), validate_cpf],
                           help_text=_("Insert your CPF Number without dots"),)

    email = models.EmailField(max_length=255,)

    objects = ReporterManager()

    def __str__(self):
        return self.name

    def clean(self):
        today = date.today()

        try:
            if "teste" in self.name.lower() :
                raise ValidationError({"name": _("Reporter must not have the word 'teste' in the name")},
                                       code="error1"
                                      )
        except ValueError:
            # TODO: deve ser tratado ainda o ano bissexto para poder usar essa função
            pass