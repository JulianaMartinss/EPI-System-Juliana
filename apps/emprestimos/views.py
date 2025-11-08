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

            if emprestimo.quantidade > epi.quantidade:
                messages.error(request, f"Estoque insuficiente. Apenas {epi.quantidade} disponíveis.")
                return redirect('listar_emprestimos')

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
