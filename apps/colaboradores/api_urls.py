from django.urls import path
from .api import ColaboradorListCreateAPI, ColaboradorRetrieveUpdateDestroyAPI

urlpatterns = [
    path('colaboradores/', ColaboradorListCreateAPI.as_view(), name='colaboradores-list-create'),
    path('colaboradores/<int:pk>/', ColaboradorRetrieveUpdateDestroyAPI.as_view(), name='colaboradores-detail'),
]
