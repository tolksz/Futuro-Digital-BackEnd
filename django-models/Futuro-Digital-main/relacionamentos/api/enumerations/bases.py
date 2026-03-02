from django.db import models

class Bases(models.TextChoices):
    SEGUNDO = 's', 'segundo'
    MINUTO = 'min', 'minuto'
    HORA = 'h', 'hora'
    DIA = 'd', 'dia'
    SEMANA = 'w', 'semana'
    MES = 'mes', 'mes'
    ANO = 'y', 'ano'