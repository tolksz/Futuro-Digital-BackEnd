from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


@api_view(['GET'])
def saudacao(request, nome:str = "aluno"):
    agora = datetime.now()
    mensagem = ""

    if agora.hour >= 6 and agora.hour < 12:
        mensagem = "bom dia"
    elif agora.hour >= 12 and agora.hour < 18:
        mensagem = "boa tarde"
    else:
        mensagem = "boa noite"

    return Response({
        'saudacao': f'{mensagem}, {nome}'

    })


class SaudacaoService(APIView):
    def get(self, request):
        return Response({'Mensagem':'Sou uma classe.'})


class OutraSaudacaoService(APIView):
    def get(self, request, nome: str = "aluno"):
        agora = datetime.now()
        mensagem = ""

        if agora.hour >= 6 and agora.hour < 12:
            mensagem = "bom dia"
        elif agora.hour >= 12 and agora.hour < 18:
            mensagem = "boa tarde"
        else:
            mensagem = "boa noite"

        return Response({
            'saudacao': f'{mensagem}, {nome}'

        })