from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.models import Projeto
from api.serializers import ProjetoSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def relatorio_anual(request, ano):
    projetos = Projeto.objects.filter(inicio__year=ano)
    serializer = ProjetoSerializer(projetos, many=True)

    return Response({
        "ano": ano,
        "projetos": serializer.data
    })