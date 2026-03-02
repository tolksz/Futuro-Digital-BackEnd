from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from digital.models import BaseModel
from digital.validators.funcoes import validar_maioridade


class Atleta(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(2, message="Tamanho minimo de 2 caracteres")],
                            help_text='Insira o nome do exemplo',
                            verbose_name='Nome do Exemplo')


    esporte = models.CharField(max_length=50,
                            validators=[MinLengthValidator(2, message="Tamanho minimo de 2 caracteres")],
                            help_text='Insira o nome do esporte',
                            verbose_name='Nome do esporte')

    nascimento = models.DateField(help_text="nascimento do atleta",
                                  verbose_name="data nasc",
                                  validators=[validar_maioridade])