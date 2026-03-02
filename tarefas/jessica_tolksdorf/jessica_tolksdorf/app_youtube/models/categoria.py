from django.db import models
from django.core.validators import MinLengthValidator


class Categoria(models.Model):
    nome = models.CharField(unique=True,
                            max_length=50,
                            validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.nome