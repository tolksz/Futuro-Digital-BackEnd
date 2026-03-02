from django.db import models

class TipoProjeto(models.TextChoices):
    WEB = 'WEB', 'Web'
    MOBILE = 'MOBILE', 'Mobile'
    API = 'API', 'API'
    DATA_SCIENCE = 'DATA_SCIENCE', 'Data Science'
    AI = 'AI', 'Inteligência Artificial'
    LIBRARY = 'LIBRARY', 'Biblioteca'
    DESKTOP = 'DESKTOP', 'Desktop'