from django.db import models

class TipoIngresso(models.TextChoices):
    NORMAL = "Inteira", "Inteira"
    HALF = "Meia Entrada", "Meia Entrada"
    VIP = "Vip", "Vip"