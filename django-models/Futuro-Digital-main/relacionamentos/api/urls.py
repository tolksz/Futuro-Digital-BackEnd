from django.urls import path
from api.views import saudacao, SaudacaoService, OutraSaudacaoService
from api.views.calculadora import CalculoService

app_name = 'api'

urlpatterns = [
    path('saudacao/', saudacao, name='saudacao'),
    path('saudacao/<str:nome>', saudacao, name='saudacao_parametro'),
    path('classe/saudacao/', SaudacaoService.as_view(), name='classe_saudacao'),

    path('classe/outrasaudacao/', OutraSaudacaoService.as_view(),
        name="clase_outrasaudacao"),

    path('calculadora/', CalculoService.as_view(), name='calculadora')
]