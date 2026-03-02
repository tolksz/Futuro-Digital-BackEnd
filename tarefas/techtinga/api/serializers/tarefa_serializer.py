from rest_framework import serializers
from core.models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = [
            'titulo', 'linguagem', 'estimativa_horas',
            'horas_registradas', 'status', 'responsavel',
            'criacao', 'conclusao'
        ]