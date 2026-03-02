from django.http import JsonResponse
from django.db.models import Sum
from .models import Projeto, Tarefa

def relatorio_anual(request, ano):
    projetos = Projeto.objects.filter(inicio__year=ano)
    lista_projetos = []

    for proj in projetos:
        tarefas = proj.tarefas.all()
        t_concluidas = tarefas.filter(status='DONE')
        t_atrasadas = tarefas.filter(status='DELAYED')

        def resumir(qs):
            return {
                "quantidade": qs.count(),
                "horas_estimadas": qs.aggregate(Sum('estimativa_horas'))['estimativa_horas__sum'] or 0,
                "horas_registradas": qs.aggregate(Sum('horas_registradas'))['horas_registradas__sum'] or 0,
                "tarefas": list(qs.values('titulo', 'linguagem', 'estimativa_horas', 'horas_registradas', 'status', 'responsavel', 'criacao', 'conclusao'))
            }

        lista_projetos.append({
            "nome": proj.nome,
            "inicio": proj.inicio,
            "previsao_termino": proj.previsao_termino,
            "orcamento": str(proj.orcamento),
            "resumo": {
                "tarefas_concluidas": resumir(t_concluidas),
                "tarefas_atrasadas": resumir(t_atrasadas)
            }
        })

    return JsonResponse({"ano": ano, "projetos": lista_projetos}, json_dumps_params={'indent': 2}) 