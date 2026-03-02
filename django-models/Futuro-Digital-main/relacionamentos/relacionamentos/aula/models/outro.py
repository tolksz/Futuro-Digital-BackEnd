from django.db import models

from aula.models import BaseModel, Paper, Magazine


class Outro(BaseModel):
    teste = models.CharField("Outro", max_length=255)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    revistas = models.ManyToManyField(Magazine)
    class Meta:
        verbose_name = "Outro"
        abstract = True