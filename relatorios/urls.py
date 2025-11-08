from django.urls import path
from . import views

urlpatterns = [
    path('colaborador/', views.relatorio_por_colaborador, name='relatorio_por_colaborador'),
    path('epi/', views.relatorio_por_epi, name='relatorio_por_epi'),
    path('vencidos/', views.relatorio_epis_vencidos, name='relatorio_epis_vencidos'),
]
