from django.db.models import QuerySet
from .base_manager import BaseManager


class ExemploManager(BaseManager):

    def find_by_nome(self, nome: str) -> QuerySet['Exemplo']:
        if isinstance(nome, str) and len(nome) > 0:
            consulta = self.filter(nome__icontains=nome)
            return consulta
        else:
            raise TypeError('O nome deve ser string')


    def find_by_cod(self, cod: str) -> list['Exemplo']:
        if isinstance(cod, str) and len(cod) == 10:
            consulta = self.filter(cod=cod)
            return list(consulta)
        else:
            raise TypeError('O cod deve ser string e conter 10 caracteres')

