from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Emprestimo
from apps.colaboradores.models import Colaborador
from apps.epi.models import EPI
from django.utils import timezone
from django.contrib import messages

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'epi', 'quantidade', 'previsao_devolucao']


@login_required
def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all().order_by('-data_emprestimo')
    return render(request, 'emprestimos/listar.html', {'emprestimos': emprestimos})


@login_required
def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            epi = emprestimo.epi

            # ❗ Bloqueia quantidade zero ou negativa
            if emprestimo.quantidade <= 0:
                messages.error(request, "A quantidade deve ser maior que zero.")
                return render(request, 'emprestimos/form.html', {
                    'form': form,
                    'titulo': 'Registrar Empréstimo'
                })

            # ❗ Bloqueia emprestar mais do que o estoque disponível
            if emprestimo.quantidade > epi.quantidade:
                quant = epi.quantidade
                txt = "disponível" if quant == 1 else "disponíveis"

                messages.error(
                    request,
                    f"Estoque insuficiente. Apenas {quant} {txt}."
                )
                return render(request, 'emprestimos/form.html', {
                    'form': form,
                    'titulo': 'Registrar Empréstimo'
                })

            # Atualiza estoque
            epi.quantidade -= emprestimo.quantidade
            epi.save()

            emprestimo.responsavel = request.user
            emprestimo.save()

            messages.success(request, "Empréstimo registrado com sucesso!")
            return redirect('listar_emprestimos')

    else:
        form = EmprestimoForm()

    return render(request, 'emprestimos/form.html', {'form': form, 'titulo': 'Registrar Empréstimo'})


@login_required
def devolver_epi(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)

    if not emprestimo.devolvido:
        emprestimo.devolvido = True
        emprestimo.epi.quantidade += emprestimo.quantidade
        emprestimo.epi.save()
        emprestimo.save()
        messages.success(request, "EPI devolvido com sucesso!")

    return redirect('listar_emprestimos')
