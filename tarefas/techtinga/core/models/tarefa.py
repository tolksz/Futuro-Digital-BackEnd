from django.db import models
from .base_model import BaseModel
from .projeto import Projeto
from core.enumerations.status_tarefa import StatusTarefa
from core.enumerations.linguagem import Linguagem


class Tarefa(BaseModel):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    linguagem = models.CharField(max_length=20, choices=Linguagem.choices, blank=True, null=True)

    estimativa_horas = models.IntegerField()
    horas_registradas = models.IntegerField(default=0)
    prioridade = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=StatusTarefa.choices, default=StatusTarefa.PENDING)

    responsavel = models.CharField(max_length=100)
    criacao = models.DateTimeField()
    conclusao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'core'