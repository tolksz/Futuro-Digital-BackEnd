from django.contrib import admin
from .models import Carro


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'placa', 'ano', 'valor_diaria', 'alugado')

    list_filter = ('marca', 'alugado', 'ipva')

    search_fields = ('modelo', 'placa')


    readonly_fields = ('seguro',)