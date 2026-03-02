from django.db import models

class StatusTarefa(models.TextChoices):
    PENDING = 'PENDING', 'Pendente'
    DONE = 'DONE', 'Concluída'
    DELAYED = 'DELAYED', 'Atrasada'
    BLOCKED = 'BLOCKED', 'Bloqueada'