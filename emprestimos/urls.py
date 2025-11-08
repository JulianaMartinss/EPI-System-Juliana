from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_emprestimos, name='listar_emprestimos'),
    path('novo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('<int:id>/devolver/', views.devolver_epi, name='devolver_epi'),
]
