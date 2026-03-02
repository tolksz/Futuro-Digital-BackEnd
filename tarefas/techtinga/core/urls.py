from django.urls import path
from . import views

urlpatterns = [
    path('api/relatorio/<int:ano>/', views.relatorio_anual),
]