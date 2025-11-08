from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)  # validar depois
    setor = models.CharField(max_length=80)
    foto_colaborador = models.ImageField(
        upload_to='colaboradores/fotos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nome} ({self.setor})"
