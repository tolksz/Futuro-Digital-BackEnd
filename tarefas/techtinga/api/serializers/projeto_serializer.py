from rest_framework import serializers
from django.db.models import Sum
from core.models import Projeto
from .tarefa_serializer import TarefaSerializer

class ProjetoSerializer(serializers.ModelSerializer):
    resumo = serializers.SerializerMethodField()

    class Meta:
        model = Projeto
        fields = ['nome', 'inicio', 'previsao_termino', 'orcamento', 'resumo']

    def get_resumo(self, obj):
        tarefas = obj.tarefas.all()
        t_concluidas = tarefas.filter(status='DONE')
        t_atrasadas = tarefas.filter(status='DELAYED')

        def montar_dados(queryset):
            return {
                "quantidade": queryset.count(),
                "horas_estimadas": queryset.aggregate(Sum('estimativa_horas'))['estimativa_horas__sum'] or 0,
                "horas_registradas": queryset.aggregate(Sum('horas_registradas'))['horas_registradas__sum'] or 0,
                "tarefas": TarefaSerializer(queryset, many=True).data
            }

        return {
            "tarefas_concluidas": montar_dados(t_concluidas),
            "tarefas_atrasadas": montar_dados(t_atrasadas)
        }