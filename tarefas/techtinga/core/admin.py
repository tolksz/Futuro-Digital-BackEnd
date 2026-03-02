from django.contrib import admin
from core.models import Projeto, Tarefa

class TarefaInline(admin.TabularInline):
    model = Tarefa
    extra = 0
    fields = ('titulo', 'status', 'responsavel')

class ProjetoAdmin(admin.ModelAdmin):
    inlines = [TarefaInline]
    list_display = ('codigo', 'nome', 'ativo')

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Tarefa)