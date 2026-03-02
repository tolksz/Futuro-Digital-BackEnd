from django.db import models

class Setor(models.TextChoices):
    STAND = "Arquibancada", "Arquibancada"
    SEAT = "Cadeira", "Cadeira"
    CABIN = "Camarote", "Camarote"
    COMMON = "Pista", "Pista"