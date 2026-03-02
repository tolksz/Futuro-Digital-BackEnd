from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from gerencia_eventos.enumerations.setor import Setor


class Assento(models.Model):
    codigo = models.CharField(max_length=3,
        validators=[MinLengthValidator(3)], verbose_name= "Código do assento",
        help_text="deve ter exatamente 3 caracteres.")

    bloco = models.IntegerField(validators=[MinValueValidator(1)],
        verbose_name="Bloco", help_text="Número do bloco onde o assento está localizado.")

    setor = models.CharField(max_length= 20, choices=Setor.choices,
        verbose_name="Setor", help_text="Área do estádio/local.")

    disponivel = models.BooleanField(default=False, verbose_name="Está disponível?",
        help_text="Se desmarcado  indica que o assento está ocupado"
    )

    preco = models.FloatField( validators=[MinValueValidator(0.00)], verbose_name="Preço do assento",
        help_text="Valor base do assento em reais (R$).")

    acessibilidade = models.BooleanField( default=False,
        verbose_name="Possui acessibilidade?",
        help_text="Marque se o assento é reservado para PCD")

    ultima_manutencao = models.DateField(null=True, blank=True,
            verbose_name="Última Manutenção",
        help_text="Data da última vistoria técnica (opcional)")

    def atualizar_disponibilidade(self):
        tem_ingresso = hasattr(self, 'ingresso')
        self.disponivel = not tem_ingresso
        self.save(update_fields=['disponivel'])

    def __str__(self):
        status = "Livre" if self.disponivel else "Ocupado"
        return f"{self.setor} - {self.codigo} ({status})"

    class Meta:
        verbose_name = "Assento"
        verbose_name_plural = "Assentos"