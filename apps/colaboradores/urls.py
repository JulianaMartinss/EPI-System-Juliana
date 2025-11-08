from django.urls import path
from . import views

app_name = 'colaboradores'

urlpatterns = [
    path('', views.ColaboradorList.as_view(), name='lista'),
    path('novo/', views.ColaboradorCreate.as_view(), name='criar'),
    path('<int:pk>/editar/', views.ColaboradorUpdate.as_view(), name='editar'),
    path('<int:pk>/excluir/', views.ColaboradorDelete.as_view(), name='excluir'),
]
