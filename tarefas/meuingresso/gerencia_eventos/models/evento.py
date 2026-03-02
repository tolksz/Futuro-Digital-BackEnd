from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils import timezone
from gerencia_eventos.enumerations.tipo_evento import TipoEvento
from gerencia_eventos.validators.validacoes import validar_capacidade_evento


class Evento(models.Model):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(5)],
        verbose_name="Nome do Evento",
        help_text="O nome deve ter no mínimo 5 caracteres.")

    descricao = models.CharField(max_length=1000, blank=True,
        null=True,verbose_name="Descrição",
        help_text="Coloque aqui um resumo sobre o evento (opcional).")

    data = models.DateField(default=timezone.now,
        verbose_name="Data do Evento",
        help_text="Data em que o evento ocorrera")

    time = models.TimeField(default=timezone.now, verbose_name="Horário",
        help_text="Horário de inicio do evento.")

    tipo_evento = models.CharField(max_length=20,
        choices=TipoEvento.choices, verbose_name="Tipo de evento",
        help_text="Selecione a categoria do evento."
    )

    capacidade = models.IntegerField( validators=[validar_capacidade_evento],
        verbose_name="Capacidade Máxima",
        help_text="Quantidade total de pessoas permitidas no evento (entre 10 e 60.000).")

    cobertura_campo = models.BooleanField(default=False, verbose_name="Cobertura de Campo?",
        help_text="Marque se o local possui cobertura contra chuva." )

    organizador = models.CharField( max_length=100, validators=[MinLengthValidator(5)],
        verbose_name="Organizador", help_text="Nome da empresa ou pessoa responsável pelo evento.")


    ingressos_disponiveis = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Ingressos Disponíveis",editable=False,
        help_text="Este campo é calculado automaticamente pelo sistema."
    )

    def save(self, *args, **kwargs):
        if self.pk is None and self.ingressos_disponiveis is None:
            self.ingressos_disponiveis = self.capacidade
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({self.data})"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"