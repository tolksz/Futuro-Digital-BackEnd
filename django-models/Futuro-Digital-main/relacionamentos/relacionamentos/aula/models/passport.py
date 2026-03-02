from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from .base_model import BaseModel
from .person import Person
from django.db import models

class Passport(BaseModel):
    number = models.CharField(max_length=10,
                              validators=[MinLengthValidator(4)],
                              unique=True,
                              verbose_name="Passport Number",
                              help_text="Passport")
    issue_date = models.DateField(verbose_name="Issue Date",)
    expiration_date = models.DateField(verbose_name="Expiration Date",)
    owner = models.OneToOneField(Person,
                                 on_delete=models.CASCADE,
                                 verbose_name="Owner",
                                 help_text="Owner")

    def __str__(self):
        return self.number

    def clean(self):
        if self.issue_date >= self.expiration_date:
            raise ValidationError(
                {"issue_date": _('Issue date must be before expiration date'),
                 "expiration_date": _('Issue date must be before expiration date')},
                code="error0101")
        if self.owner.birthdate > self.issue_date:
            raise ValidationError(
                {"issue_date": _('Owner birthdate must be before of the passport issue date'),},
                code="error0102")