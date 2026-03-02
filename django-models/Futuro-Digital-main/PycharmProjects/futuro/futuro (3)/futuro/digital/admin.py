from django.contrib import admin
from digital.models import Exemplo
from digital.models.atleta import Atleta

# Register your models here.
admin.site.register(Exemplo)
admin.site.register(Atleta)