from django.contrib import admin
from .models import EPI

@admin.register(EPI)
class EPIAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'quantidade', 'validade')
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria', 'validade')
