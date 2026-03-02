from django.urls import path
from api.views import saudacao

app_name = 'api'

urlpatterns = [
    path('saudacao/', saudacao, name='saudacao'),
    path('saudacao/<str:nome>', saudacao, name='saudacao_parametro')

]