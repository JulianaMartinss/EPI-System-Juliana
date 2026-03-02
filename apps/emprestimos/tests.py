from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from apps.colaboradores.models import Colaborador
from apps.epi.models import EPI
from apps.emprestimos.models import Emprestimo
from django.utils import timezone

class EmprestimoViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='123')
        self.client.login(username='test', password='123')

        self.colaborador = Colaborador.objects.create(nome="João")
        self.epi = EPI.objects.create(nome="Capacete", quantidade=10)

    def test_listar_emprestimos(self):
        response = self.client.get(reverse('listar_emprestimos'))
        self.assertEqual(response.status_code, 200)

    def test_criar_emprestimo_valido(self):
        response = self.client.post(reverse('criar_emprestimo'), {
            'colaborador': self.colaborador.id,
            'epi': self.epi.id,
            'quantidade': 2,
            'previsao_devolucao': timezone.now().date()
        })

        self.assertEqual(response.status_code, 302)  # redirect
        self.epi.refresh_from_db()
        self.assertEqual(self.epi.quantidade, 8)

    def test_quantidade_zero(self):
        response = self.client.post(reverse('criar_emprestimo'), {
            'colaborador': self.colaborador.id,
            'epi': self.epi.id,
            'quantidade': 0,
            'previsao_devolucao': timezone.now().date()
        })

        self.assertEqual(response.status_code, 200)

    def test_quantidade_maior_que_estoque(self):
        response = self.client.post(reverse('criar_emprestimo'), {
            'colaborador': self.colaborador.id,
            'epi': self.epi.id,
            'quantidade': 20,
            'previsao_devolucao': timezone.now().date()
        })

        self.assertEqual(response.status_code, 200)

    def test_devolver_epi(self):
        emprestimo = Emprestimo.objects.create(
            colaborador=self.colaborador,
            epi=self.epi,
            quantidade=2,
            previsao_devolucao=timezone.now().date(),
            responsavel=self.user
        )

        self.client.get(reverse('devolver_epi', args=[emprestimo.id]))

        emprestimo.refresh_from_db()
        self.assertTrue(emprestimo.devolvido)