from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'epi', 'quantidade', 'data_emprestimo', 'devolvido')
    list_filter = ('devolvido', 'data_emprestimo')
    search_fields = ('colaborador__nome', 'epi__nome')
