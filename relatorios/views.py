from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.colaboradores.models import Colaborador
from apps.epi.models import EPI
from apps.emprestimos.models import Emprestimo
from django.utils import timezone

@login_required
def relatorio_por_colaborador(request):
    colaboradores = Colaborador.objects.all().order_by('nome')
    colaborador_id = request.GET.get('colaborador')
    emprestimos = Emprestimo.objects.all().order_by('-data_emprestimo')

    if colaborador_id:
        emprestimos = emprestimos.filter(colaborador_id=colaborador_id)

    context = {
        'colaboradores': colaboradores,
        'emprestimos': emprestimos,
        'colaborador_id': colaborador_id
    }
    return render(request, 'relatorios/por_colaborador.html', context)

@login_required
def relatorio_por_epi(request):
    epis = EPI.objects.all().order_by('nome')
    epi_id = request.GET.get('epi')
    emprestimos = Emprestimo.objects.all().order_by('-data_emprestimo')

    if epi_id:
        emprestimos = emprestimos.filter(epi_id=epi_id)

    context = {
        'epis': epis,
        'emprestimos': emprestimos,
        'epi_id': epi_id
    }
    return render(request, 'relatorios/por_epi.html', context)

@login_required
def relatorio_epis_vencidos(request):
    hoje = timezone.now().date()
    epis_vencidos = EPI.objects.filter(validade__lt=hoje).order_by('validade')

    context = {'epis_vencidos': epis_vencidos}
    return render(request, 'relatorios/epis_vencidos.html', context)
