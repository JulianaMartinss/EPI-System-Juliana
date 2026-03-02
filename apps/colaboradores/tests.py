from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from apps.colaboradores.models import Colaborador
from apps.epi.models import EPI
from apps.emprestimos.models import Emprestimo
from datetime import date

class ColaboradorViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='123')
        self.client.login(username='test', password='123')

        self.colaborador = Colaborador.objects.create(
            nome="João",
            cpf="12345678900",
            setor="RH"
        )

    def test_home_view(self):
        # cria dados para o dashboard
        EPI.objects.create(nome="Capacete", categoria="capacete", quantidade=5, validade=date(2026,1,1))
        Emprestimo.objects.create(
            colaborador=self.colaborador,
            epi=EPI.objects.first(),
            quantidade=1,
            previsao_devolucao=date(2026,1,10),
            responsavel=self.user
        )

        response = self.client.get(reverse('colaboradores:home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_epis', response.context)
        self.assertIn('emprestados', response.context)
        self.assertIn('devolvidos', response.context)

    def test_list_view(self):
        response = self.client.get(reverse('colaboradores:lista'))
        self.assertEqual(response.status_code, 200)

    def test_create_colaborador(self):
        response = self.client.post(reverse('colaboradores:criar'), {
            'nome': "Maria",
            'cpf': "98765432100",
            'setor': "Financeiro",
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Colaborador.objects.count(), 2)

    def test_update_colaborador(self):
        response = self.client.post(
            reverse('colaboradores:editar', args=[self.colaborador.id]),
            {
                'nome': "João Editado",
                'cpf': "12345678900",
                'setor': "TI",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.colaborador.refresh_from_db()
        self.assertEqual(self.colaborador.nome, "João Editado")

    def test_delete_colaborador(self):
        response = self.client.post(
            reverse('colaboradores:excluir', args=[self.colaborador.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Colaborador.objects.count(), 0)