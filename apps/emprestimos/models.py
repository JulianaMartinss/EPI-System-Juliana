from django.db import models
from django.contrib.auth.models import User
from apps.colaboradores.models import Colaborador
from apps.epi.models import EPI
from django.utils import timezone

class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    epi = models.ForeignKey(EPI, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_emprestimo = models.DateTimeField(default=timezone.now)
    previsao_devolucao = models.DateField()
    devolvido = models.BooleanField(default=False)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.colaborador.nome} - {self.epi.nome}"

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
