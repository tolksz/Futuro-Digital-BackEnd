from django.db import models


class Operador(models.TextChoices):
    ADICAO = '+', 'Adição'
    SUBTRACAO = '-', 'Subtração'
    MULTIPLICACAO = '*', 'Multiplicação'
    DIVISAO = '/', 'Divisão'
    EXPONENCIACAO = '**', 'Exponenciacao'
    RAIZ = 'V', 'Raíz'
    PORCENTAGEM = '%', 'Porcentagem'
    MODULO= '%%', 'Módulo'