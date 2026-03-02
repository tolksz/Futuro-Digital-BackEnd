import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from core.models import Projeto, Tarefa
from django.utils.timezone import make_aware


class Command(BaseCommand):
    help = 'Importa techtinga.csv'

    def handle(self, *args, **kwargs):
        def tentar_converter_data(data_str):
            if not data_str: return None
            formatos = ['%Y-%m-%dT%H:%M:%S', '%d/%m/%Y', '%Y-%m-%d', '%d/%m/%Y %H:%M:%S']
            for fmt in formatos:
                try:
                    return make_aware(datetime.strptime(data_str, fmt))
                except ValueError:
                    continue
            return None

        try:
            with open('techtinga.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if not row.get('projeto_codigo'): continue



                    inicio = datetime.strptime(row['projeto_inicio'],
                                               '%Y-%m-%d').date() if '-' in row[
                        'projeto_inicio'] else datetime.strptime(row['projeto_inicio'],
                '%d/%m/%Y').date()
                    prev = datetime.strptime(row['projeto_previsao_termino'],
                                             '%Y-%m-%d').date() if '-' in row[
                        'projeto_previsao_termino'] else datetime.strptime(row
                    ['projeto_previsao_termino'],'%d/%m/%Y').date()



                    projeto, _ = Projeto.objects.get_or_create(
                        codigo=row['projeto_codigo'],
                        defaults={
                            'nome': row['projeto_nome'],
                            'tipo_projeto': row['projeto_tipo_projeto'],
                            'cliente': row['projeto_cliente'],
                            'gerente': row['projeto_gerente'],
                            'inicio': inicio,
                            'previsao_termino': prev,
                            'orcamento': row['projeto_orcamento'],
                            'ativo': row['projeto_ativo'] == 'True'
                        }
                    )

                    if row.get('tarefa_titulo'):
                        Tarefa.objects.create(
                            projeto=projeto,
                            titulo=row['tarefa_titulo'],
                            descricao=row.get('tarefa_descricao', ''),
                            linguagem=row['tarefa_linguagem'],
                            estimativa_horas=int(row['tarefa_estimativa_horas']),
                            horas_registradas=int(row['tarefa_horas_registradas']),
                            prioridade=int(row['tarefa_prioridade']),
                            status=row['tarefa_status'],
                            responsavel=row['tarefa_responsavel'],
                            criacao=tentar_converter_data(row['tarefa_criacao']),
                            conclusao=tentar_converter_data(row['tarefa_conclusao'])
                        )
            self.stdout.write(self.style.SUCCESS('Dados importados!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro: {e}'))