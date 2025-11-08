from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_epis, name='listar_epis'),
    path('novo/', views.criar_epi, name='criar_epi'),
    path('<int:id>/editar/', views.editar_epi, name='editar_epi'),
    path('<int:id>/excluir/', views.excluir_epi, name='excluir_epi'),
]
