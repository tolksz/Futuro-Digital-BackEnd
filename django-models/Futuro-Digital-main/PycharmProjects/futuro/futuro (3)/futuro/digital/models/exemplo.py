from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from digital.enumerations import Campus
from digital.models import BaseModel
from digital.validators.funcoes import validar_maioridade
from digital.validators.nome_proibido_validator import NomeProibidoValidator



class Exemplo(BaseModel):
    nome = models.CharField(max_length=100,
                            validators = [MinLengthValidator(2, message="Tamanho minimo de 2 caracteres"),
                            NomeProibidoValidator(nomes_proibidos=["admin", "root"])],
                            help_text='Insira o nome do exemplo',
                            verbose_name='Nome do Exemplo')

    apelido = models.CharField(max_length=100, null=True, blank = True,
                            validators = [MinLengthValidator(2, message="Tamanho minimo de 2 caracteres")],
                            help_text='Insira o apelido',
                            verbose_name='apelido')


    idade = models.IntegerField(help_text="Idade do Exemplo", null= True, blank = True,
                                verbose_name="Idade",
                                 validators = [
                                     MinValueValidator(18, message="idade minima"),
                                     MaxValueValidator(100, message="idade máxima de 100 anos")]
                                 )

    cpf = models.CharField(max_length=100, default = -1, null= True, blank = True,
                            validators = [MinLengthValidator(11, message="Tamanho minimo de 11 caracteres")],
                            help_text='Cadastro de Pessoa Física',
                            verbose_name='Insira o número do seu CPF sem ponto.')

    nascimento = models.DateField(help_text="nascimento do atleta", null= True, blank = True,
                                verbose_name="data nasc",
                                validators=[validar_maioridade])

    campus = models.CharField(max_length=30, null= True, blank = True, help_text = "digite o campus de sua escolha",
                              verbose_name= "campus", validators = [MinLengthValidator(3)], choices = Campus, default= Campus.PORTO_ALEGRE,
                              )


    def __str__(self):
        return f"{self.id} - {self.nome}"

# metodo que permmite realizar validacoes cross-field (ou diversos campos)
    def clean(self):
        if self.nascimento != None and self.nascimento != "":
            hoje = date.today()
            idade_calculada = int((hoje - self.nascimento)/365.25)
            if idade_calculada != self.idade:
                raise ValidationError({
                    "idade": "idade incorreta para o nascimento informado",
                    "nascimento": "nascimento incorreto para a idade informada"

            })
        if self.apelido != None and self.apelido != "":
            if self.nome.lower()==self.apelido.lower():
                raise ValidationError({
                "apelido": "apelido nao pode ser igual ao nome"

        })
#metodo que permite alterar campos antes de realizar a persistencia dos dados
def save(self, *args, **kargs):
    if self.nascimento == None or self.nascimento == "":
        hoje = date.today()
        data_nascimento_calculada = hoje.replace(year=hoje.year - self.idade)
        self.nascimento = data_nascimento_calculada

    super().save(*args, **kargs)


class Meta:
    ordering=["nome"]