from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from apps.epi.models import EPI
from datetime import date

class EPIViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='123')
        self.client.login(username='test', password='123')

        self.epi = EPI.objects.create(
            nome="Capacete",
            categoria="capacete",
            quantidade=10,
            validade=date(2026, 1, 1),
            descricao="Proteção para cabeça"
        )

    def test_listar_epis(self):
        response = self.client.get(reverse('listar_epis'))
        self.assertEqual(response.status_code, 200)

    def test_criar_epi_get(self):
        response = self.client.get(reverse('criar_epi'))
        self.assertEqual(response.status_code, 200)

    def test_criar_epi_post(self):
        response = self.client.post(reverse('criar_epi'), {
            'nome': "Luva",
            'categoria': "luva",
            'quantidade': 5,
            'validade': '2027-01-01',
            'descricao': "Luva de proteção"
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(EPI.objects.count(), 2)

    def test_editar_epi(self):
        response = self.client.post(reverse('editar_epi', args=[self.epi.id]), {
            'nome': "Capacete Editado",
            'categoria': "capacete",
            'quantidade': 15,
            'validade': '2026-01-01',
            'descricao': "Atualizado"
        })

        self.assertEqual(response.status_code, 302)
        self.epi.refresh_from_db()
        self.assertEqual(self.epi.nome, "Capacete Editado")

    def test_excluir_epi_get(self):
        response = self.client.get(reverse('excluir_epi', args=[self.epi.id]))
        self.assertEqual(response.status_code, 200)

    def test_excluir_epi_post(self):
        response = self.client.post(reverse('excluir_epi', args=[self.epi.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(EPI.objects.count(), 0)