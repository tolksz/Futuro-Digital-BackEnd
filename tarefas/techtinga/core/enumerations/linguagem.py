from django.db import models

class Linguagem(models.TextChoices):
    PYTHON = 'PYTHON', 'Python'
    JS = 'JS', 'JavaScript'
    JAVA = 'JAVA', 'Java'
    DART = 'DART', 'Dart'
    PHP = 'PHP', 'PHP'
    C = 'C', 'C'
    OUTRO = 'OUTRO', 'Outro'