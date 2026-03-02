from django.db import models


class Visibilidade(models.TextChoices):
    PUBLICO = 'PUBLICO', 'Público'
    PRIVADO = 'PRIVADO', 'Privado'
    NAO_LISTADO = 'NAO_LISTADO', 'Não Listado'