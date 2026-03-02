from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal
import datetime

MIN_VALORES_MARCA = {
    'Porsche': 2000,
    'Ferrari': 1500,
    'Ford': 200,
    'Lamborghini': 2000,
    'Tesla': 500,
    'Bugatti': 5000,
}


def calcular_valor_seguro(valor_diaria):
    if not valor_diaria:
        return Decimal('0.00')
    calculo = valor_diaria * Decimal('0.05')
    return max(calculo, Decimal('50.00'))


def validar_preco_minimo_marca(marca, valor_diaria):
    min_val = MIN_VALORES_MARCA.get(marca, 200)
    if valor_diaria < min_val:
        raise ValidationError({
            'valor_diaria': f"O valor minimo para {marca} é R$ {min_val}."
        })


def validar_ano_carro(ano):
    today = timezone.now().date()
    current_year = today.year
    if not (current_year - 5 <= ano <= current_year + 1):
        raise ValidationError(f"O ano deve estar entre {current_year - 5} e {current_year + 1}.")


def validar_data_revisao(data_revisao):
    today = timezone.now().date()
    if data_revisao > today:
        raise ValidationError("A data da última revisão não pode ser futura.")


def validar_condicoes_para_alugar(carro_obj):
    if not carro_obj.alugado:
        return

    erros = {}

    if not carro_obj.ipva:
        erros['ipva'] = "Carros com IPVA atrasado não podem ser alugados."

    if carro_obj.ultima_revisao:
        today = timezone.now().date()
        um_ano_atras = today - datetime.timedelta(days=365)
        if carro_obj.ultima_revisao < um_ano_atras:
            erros['ultima_revisao'] = "Carros com vistoria há mais de um ano não podem ser alugados."


    if erros:
        raise ValidationError(erros)

