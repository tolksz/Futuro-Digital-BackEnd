from rest_framework import serializers
from api.enumerations import Operador


class OperacaoSerializer(serializers.Serializer):
    primeiro_termo = serializers.FloatField(required=True)
    segundo_termo = serializers.FloatField(required=True)
    operador = serializers.ChoiceField(required=True, choices = Operador.choices)

    resultado = serializers.FloatField(required=False)

    class Meta:
        #fields que serao aproveitados do request
        fields = ['primeiro_termo', 'segundo_termo', 'operador']


    def calcular(self):
        primeiro_termo = self.validated_data.get('primeiro_termo')
        segundo_termo = self.validated_data.get('segundo_termo')
        operador = self.validated_data.get('operador')

        match operador:
            case Operador.ADICAO:
                resultado = primeiro_termo + segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.ADICAO.label})

            case Operador.SUBTRACAO:
                resultado = primeiro_termo - segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.SUBTRACAO.label})

            case Operador.MULTIPLICACAO:
                resultado = primeiro_termo * segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.MULTIPLICACAO.label})

            case Operador.DIVISAO:
                resultado = primeiro_termo / segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.DIVISAO.label})

            case Operador.EXPONENCIACAO:
                resultado = primeiro_termo ** segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.EXPONENCIACAO.label})

            case Operador.RAIZ:
                resultado = primeiro_termo**(1/segundo_termo)
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.RAIZ.label})

            case Operador.PORCENTAGEM:
                resultado = primeiro_termo *segundo_termo / 100
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.PORCENTAGEM.label})

            case Operador.MODULO:
                resultado = primeiro_termo % segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.MODULO.label})