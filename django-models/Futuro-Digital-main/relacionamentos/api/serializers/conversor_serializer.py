from rest_framework import serializers
from api.enumerations import Bases

class ConversorSerializer(serializers.Serializer):
    unidade = serializers.FloatField(required=True)
    base = serializers.ChoiceField(choices=Bases, required=True)
    base_destino = serializers.ChoiceField(choices=Bases, required=True)

    
