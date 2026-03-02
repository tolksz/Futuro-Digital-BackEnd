from django.db import models

from aula.models import Outro


class Teste(Outro):
    teste = models.CharField("Teste", max_length=255)
    class Meta:
        verbose_name = "Teste"