import random
import string

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from . import Paper, Reporter
from .person import Person
from .base_model import BaseModel
from aula.validators import CodValidator
from aula.validators import validate_par
from ..managers.exemplo_manager import ExemploManager


class Exemplo(BaseModel):
    cod = models.CharField(max_length=10,
                           help_text="Digite o cod\ para o exemplo (opcional)",
                           validators=[MinLengthValidator(10),
                                       CodValidator("4444444444"), validate_par],
                           blank=True)
    nome = models.CharField(max_length=15,
                            help_text="Digite o nome para o exemplo (opcional)",
                            validators=[MinLengthValidator(3)])
    people = models.ManyToManyField(Person, blank=True, null=True, related_name='people')
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)


    objects = ExemploManager()


    class Meta:
        permissions = [
            ('generate_code_exemplo', "can generate new codes")
        ]

    def __str__(self):
        return f"{self.cod } - {self.nome}"

    def save(self, *args, **kargs):
        if self.cod is None or self.cod == '':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(10))
        super().save(*args, **kargs)

    def clean(self):
        # Pode ser realizada aqui novas validações
        if not isinstance(str(self.nome), str):
            raise ValidationError({
                "nome": 'Nome informado é do  tipo errado'},
                code="error001")
        elif self.nome == "Teste":
            raise ValidationError(
                {"nome": 'Não é possível salvar testes!'},
                code="error002")
        elif self.cod == "1111111111" and self.nome == "IFRS Restinga":
            raise ValidationError(
                {"nome": 'Combinação de nome e código errada!',
                 "cod": 'Combinação de nome e código errada!'},
                code="error0101")
