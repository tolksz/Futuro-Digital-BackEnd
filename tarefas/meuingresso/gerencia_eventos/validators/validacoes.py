from django.core.exceptions import ValidationError

def validar_capacidade_evento(value):
    if not (10 <= value <= 60000):
        raise ValidationError("A capacidade deve ser entre 10 e 60.000 pessoas")

def validar_acesso_ingresso(data_acesso, data_compra, data_evento):


    if not data_acesso or not data_compra or not data_evento:
        return

    # r: acesso não pode ser anterior a compra
    if data_acesso < data_compra:
        raise ValidationError({
            'acesso': "O acesso não pode ser anterior à data de compra."
        })

    # r: acesso não pode ser depois da data do evento
    if data_acesso.date() > data_evento:
        raise ValidationError({
            'acesso': "A data de acesso não pode ser posterior a data do evento."
        })

def validar_checkin_pagamento(checkin_realizado, forma_pagamento):

    if checkin_realizado and not forma_pagamento:
        raise ValidationError({
            'checkin': "O check-in só pode ser realizado mediante confirmação de pagamento."
        })