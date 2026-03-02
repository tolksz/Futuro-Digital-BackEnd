from django.db import models

class TipoEvento(models.TextChoices):
    MATCH = "Jogo", "Jogo"
    CONCERT = "Show de Música", "Show de Música"
    OTHER = "Outros", "Outros"