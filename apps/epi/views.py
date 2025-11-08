from django.shortcuts import render, redirect, get_object_or_404
from .models import EPI
from django.contrib.auth.decorators import login_required
from django import forms

# Formulário Django para o EPI
class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nome', 'categoria', 'quantidade', 'validade', 'descricao']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }

@login_required
def listar_epis(request):
    epis = EPI.objects.all()
    return render(request, 'epi/listar.html', {'epis': epis})

@login_required
def criar_epi(request):
    if request.method == 'POST':
        form = EPIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_epis')
    else:
        form = EPIForm()
    return render(request, 'epi/form.html', {'form': form, 'titulo': 'Cadastrar EPI'})

@login_required
def editar_epi(request, id):
    epi = get_object_or_404(EPI, id=id)
    if request.method == 'POST':
        form = EPIForm(request.POST, instance=epi)
        if form.is_valid():
            form.save()
            return redirect('listar_epis')
    else:
        form = EPIForm(instance=epi)
    return render(request, 'epi/form.html', {'form': form, 'titulo': 'Editar EPI'})

@login_required
def excluir_epi(request, id):
    epi = get_object_or_404(EPI, id=id)
    if request.method == 'POST':
        epi.delete()
        return redirect('listar_epis')
    return render(request, 'epi/excluir.html', {'epi': epi})
