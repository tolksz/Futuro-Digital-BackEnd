from django.db import models

class Pagamento(models.TextChoices):
    CREDIT_CARD = "Cartão de Crédito", "Cartão de Crédito"
    MONEY = "Dinheiro", "Dinheiro"
    PIX = "Pix", "Pix"