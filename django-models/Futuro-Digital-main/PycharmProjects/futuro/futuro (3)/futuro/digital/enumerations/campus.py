from django.db import models

class Campus(models.TextChoices):
    PORTO_ALEGRE = "POA", "Campus Porto Alegre"
    RESTINGA = "Restinga", "Campus Restinga"
    ROLANTE = "Rolante", "Campus Rolante"
    ZONA_NORTE = "POA Zona Norte", "Campus POA Zona Norte"