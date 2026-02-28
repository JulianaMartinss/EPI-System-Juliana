from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from apps.colaboradores.models import Colaborador
from apps.epi.models import EPI
from apps.emprestimos.models import Emprestimo


class RelatorioPorColaboradorTests(TestCase):
    def setUp(self):
        # Criar usuário para autenticação
        self.user = User.objects.create_user(username="tester", password="12345")
        self.client.login(username="tester", password="12345")

        # Criar dados de teste
        self.colaborador = Colaborador.objects.create(nome="Maria", cpf="12345678900")
        self.epi = EPI.objects.create(nome="Capacete", validade=timezone.now().date())
        self.emprestimo = Emprestimo.objects.create(
            colaborador=self.colaborador,
            epi=self.epi,
            data_emprestimo=timezone.now(),
            previsao_devolucao=timezone.now() + timedelta(days=7),
            quantidade=1
        )

    def test_relatorio_por_colaborador_sem_filtro(self):
        response = self.client.get(reverse("relatorio_por_colaborador"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.emprestimo, response.context["emprestimos"])
        self.assertTemplateUsed(response, "relatorios/por_colaborador.html")

    def test_relatorio_por_colaborador_com_filtro(self):
        response = self.client.get(reverse("relatorio_por_colaborador"), {"colaborador": self.colaborador.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["emprestimos"]), [self.emprestimo])
        self.assertTemplateUsed(response, "relatorios/por_colaborador.html")



class RelatorioPorEPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester2", password="12345")
        self.client.login(username="tester2", password="12345")

        self.colaborador = Colaborador.objects.create(nome="João", cpf="98765432100")
        self.epi = EPI.objects.create(nome="Luva", validade=timezone.now().date())
        self.emprestimo = Emprestimo.objects.create(
            colaborador=self.colaborador,
            epi=self.epi,
            data_emprestimo=timezone.now(),
            previsao_devolucao=timezone.now() + timedelta(days=7),
            quantidade=1
        )

    def test_relatorio_por_epi_sem_filtro(self):
        response = self.client.get(reverse("relatorio_por_epi"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.emprestimo, response.context["emprestimos"])
        self.assertTemplateUsed(response, "relatorios/por_epi.html")

    def test_relatorio_por_epi_com_filtro(self):
        response = self.client.get(reverse("relatorio_por_epi"), {"epi": self.epi.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["emprestimos"]), [self.emprestimo])



class RelatorioEPIsVencidosTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester3", password="12345")
        self.client.login(username="tester3", password="12345")

        self.epi_vencido = EPI.objects.create(
            nome="Óculos",
            validade=timezone.now().date() - timezone.timedelta(days=1)
        )
        self.epi_valido = EPI.objects.create(
            nome="Botina",
            validade=timezone.now().date() + timezone.timedelta(days=10)
        )

    def test_relatorio_epis_vencidos(self):
        response = self.client.get(reverse("relatorio_epis_vencidos"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.epi_vencido, response.context["epis_vencidos"])
        self.assertNotIn(self.epi_valido, response.context["epis_vencidos"])
        self.assertTemplateUsed(response, "relatorios/epis_vencidos.html")


class FluxoCompletoTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester_fluxo", password="12345")
        self.client.login(username="tester_fluxo", password="12345")
        self.colaborador = Colaborador.objects.create(nome="Carlos", cpf="11122233344")
        self.epi = EPI.objects.create(nome="Protetor Auricular", validade=timezone.now().date())
        self.emprestimo = Emprestimo.objects.create(
            colaborador=self.colaborador,
            epi=self.epi,
            data_emprestimo=timezone.now(),
            previsao_devolucao=timezone.now() + timedelta(days=7),
            quantidade=1
        )

    def test_fluxo_relatorio_por_colaborador(self):
        response = self.client.get(reverse("relatorio_por_colaborador"), {"colaborador": self.colaborador.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["emprestimos"]), [self.emprestimo])

    def test_fluxo_relatorio_por_epi(self):
        response = self.client.get(reverse("relatorio_por_epi"), {"epi": self.epi.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["emprestimos"]), [self.emprestimo])




