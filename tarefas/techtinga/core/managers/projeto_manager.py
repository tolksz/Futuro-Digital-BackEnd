from django.db import models


class ProjetoManager(models.Manager):
    def ativos(self):
        return self.get_queryset().filter(ativo=True)

    def por_ano(self, ano):
        return self.get_queryset().filter(inicio__year=ano)