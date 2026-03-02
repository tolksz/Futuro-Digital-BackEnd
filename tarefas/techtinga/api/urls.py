from django.urls import path
from . import views

urlpatterns = [
    path('relatorio/<int:ano>/', views.relatorio_anual),
]