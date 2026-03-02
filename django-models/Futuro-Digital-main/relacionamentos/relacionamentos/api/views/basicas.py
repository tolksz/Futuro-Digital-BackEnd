from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

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