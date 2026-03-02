from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

from gerencia_eventos.enumerations.tipo_ingresso import TipoIngresso
from gerencia_eventos.enumerations.pagamento import Pagamento
from gerencia_eventos.models.evento import Evento
from gerencia_eventos.models.assento import Assento
from gerencia_eventos.validators.validacoes import (validar_acesso_ingresso, validar_checkin_pagamento)


class Ingresso(models.Model):
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, related_name='ingressos',
        help_text="Selecione o evento para este ingresso")

    assento = models.OneToOneField(
        Assento, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Assento Marcado",
        help_text="Deixe em branco para ingressos de Pista(opcional)")

    nome = models.CharField(max_length=150,
        validators=[MinLengthValidator(10)],
        verbose_name="Nome do Titular",
        help_text="Nome completo (mínimo 10 caracteres)"
    )

    email = models.EmailField(
        verbose_name="E-mail",
        help_text="Endereço para envio do comprovante.")

    data_compra = models.DateTimeField(default=timezone.now,
        verbose_name="Data da Compra")

    preco = models.FloatField(validators=[MinValueValidator(0)],
        verbose_name="Valor Pago", help_text="Preço final pago pelo cliente")

    tipo_ingresso = models.CharField(max_length=20, choices=TipoIngresso.choices,
        verbose_name="Tipo de Ingresso", help_text="Inteira, Meia ou VIP." )

    pagamento = models.CharField(max_length=20, choices=Pagamento.choices,
        verbose_name="Forma de Pagamento",
        help_text="Método utilizado para quitar o ingresso.")

    checkin = models.BooleanField(default=False, verbose_name="Check-in Realizado",
        help_text="marque apenas se o pagamento foi confirmado e o cliente entrou")

    acesso = models.DateTimeField(null=True, blank=True,
        verbose_name="Data/Hora do Acesso",
        help_text="Momento exato da entrada (catraca)."
    )

    def clean(self):
        super().clean()
        validar_checkin_pagamento(self.checkin, self.pagamento)
        if self.evento_id:
            validar_acesso_ingresso(self.acesso, self.data_compra, self.evento.data)
        if not self.pk and self.evento_id:
            if self.evento.ingressos_disponiveis <= 0:
                raise ValidationError("Não há mais ingressos disponíveis para este evento.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

        total_vendidos = self.evento.ingressos.count()
        self.evento.ingressos_disponiveis = self.evento.capacidade - total_vendidos
        self.evento.save()

        if self.assento:
            self.assento.atualizar_disponibilidade()

    def delete(self, *args, **kwargs):
        evento_ref = self.evento
        assento_ref = self.assento
        super().delete(*args, **kwargs)

        total_vendidos = evento_ref.ingressos.count()
        evento_ref.ingressos_disponiveis = evento_ref.capacidade - total_vendidos
        evento_ref.save()

        if assento_ref:
            assento_ref.atualizar_disponibilidade()

    def __str__(self):
        return f"Ingresso: {self.nome} - {self.evento.nome}"

    class Meta:
        verbose_name = "Ingresso"
        verbose_name_plural = "Ingressos"