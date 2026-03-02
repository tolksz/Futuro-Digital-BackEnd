from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible

class NomeProibidoValidator:
    def __init__ (self, nomes_proibidos=[]):
        if not isinstance(nomes_proibidos, list):
            raise TypeError("Parametros deve ser uma lista")

        self.nomes_proibidos = nomes_proibidos

        #logica do validador
    def __call__(self, valor):
        if valor in self.nomes_proibidos:
            raise ValidationError(
                "nome proibido", params = {"valor": valor}
            )

    def __eq__(self, other):
        return(
                isinstance(other, NomeProibidoValidator)
                and self.nomes_proibidos == other.nomes_proibidos)
    