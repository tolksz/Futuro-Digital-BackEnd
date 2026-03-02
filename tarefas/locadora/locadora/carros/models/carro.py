from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from carros.enumerations.marca import Marca
from carros.validators import (validar_ano_carro, validar_data_revisao,
    calcular_valor_seguro, validar_preco_minimo_marca,
    validar_condicoes_para_alugar
)


class Carro(models.Model):
    marca = models.CharField(
        max_length=20,
        choices=Marca.choices,
        validators=[MinLengthValidator(4)],
        verbose_name="Marca",
        help_text="Selecione a marca do carro"
    )

    modelo = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
        verbose_name="Modelo",
        help_text="Insira o modelo do carro"
    )

    ano = models.IntegerField(
        validators=[validar_ano_carro],  # Usa a função importada lá em cima
        verbose_name="Ano",
        help_text="Insira o ano do carro"
    )

    alugado = models.BooleanField(
        default=False,
        verbose_name="Carro está alugado?",
        help_text="Marque só se o carro estiver alugado"
    )

    placa = models.CharField(
        max_length=7,
        validators=[MinLengthValidator(7)],
        verbose_name="Placa",
        help_text="Insira a placa do carro (com 7 caracteres e sem traços)"
    )

    valor_diaria = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(Decimal('50.00'))],
        verbose_name="Valor da diaria (R$)",
        help_text="Insira o valor cobrado por dia de aluguel"
    )

    seguro = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        verbose_name="Valor do Seguro (R$)",
        help_text="Campo automático: 5% do valor da diária (mínimo R$ 50,00)"
    )

    ultima_revisao = models.DateField(
        validators=[validar_data_revisao],
        verbose_name="Data da ultima revisão",
        help_text="Insira a data em que foi feita a última vistoria"
    )

    ipva = models.BooleanField(
        default=True,
        verbose_name="O IPVA esta pago?",
        help_text="Mantenha marcado se estiver em dia"
    )

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

    def clean(self):
        super().clean()

        if not self.marca or not self.valor_diaria:
            return


        validar_preco_minimo_marca(self.marca, self.valor_diaria)
        validar_condicoes_para_alugar(self)

    def save(self, *args, **kwargs):
        self.seguro = calcular_valor_seguro(self.valor_diaria)

        self.full_clean()
        super().save(*args, **kwargs)