from django.db import models
from django.core.exceptions import ValidationError
from .base_model import BaseModel
from core.enumerations.tipo_projeto import TipoProjeto
from core.managers.projeto_manager import ProjetoManager


class Projeto(BaseModel):
    objects = ProjetoManager()

    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    tipo_projeto = models.CharField(max_length=20, choices=TipoProjeto.choices)

    cliente = models.CharField(max_length=100)
    gerente = models.CharField(max_length=100)
    inicio = models.DateField()
    previsao_termino = models.DateField()
    fim = models.DateField(null=True, blank=True)
    orcamento = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def clean(self):
        if self.previsao_termino and self.inicio and self.previsao_termino < self.inicio:
            raise ValidationError('A previsão não pode ser anterior ao início.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

    class Meta:
        app_label = 'core'