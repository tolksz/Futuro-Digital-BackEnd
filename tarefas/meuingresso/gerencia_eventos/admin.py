from django.contrib import admin
from gerencia_eventos.models.evento import Evento
from gerencia_eventos.models.ingresso import Ingresso
from gerencia_eventos.models.assento import Assento

# mostrar o campo "ingressos_disponiveis"
class EventoAdmin(admin.ModelAdmin):
    readonly_fields = ('ingressos_disponiveis',)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Ingresso)
admin.site.register(Assento)