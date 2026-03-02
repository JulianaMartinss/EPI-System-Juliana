from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import EPI


# ==============================
# FORMULÁRIO DO EPI
# ==============================
class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nome', 'categoria', 'quantidade', 'validade', 'descricao']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }


# ==============================
# LISTAR EPIs
# ==============================
@login_required
def listar_epis(request):
    epis = EPI.objects.all()
    return render(request, 'epi/listar.html', {'epis': epis})


# ==============================
# CRIAR EPI
# ==============================
@login_required
def criar_epi(request):
    if request.method == 'POST':
        form = EPIForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✔ EPI cadastrado com sucesso!")
            return redirect('listar_epis')
        else:
            messages.error(request, "Erro ao cadastrar EPI. Verifique os campos.")
    else:
        form = EPIForm()

    return render(request, 'epi/form.html', {
        'form': form,
        'titulo': 'Cadastrar EPI'
    })


# ==============================
# EDITAR EPI
# ==============================
@login_required
def editar_epi(request, id):
    epi = get_object_or_404(EPI, id=id)

    if request.method == 'POST':
        form = EPIForm(request.POST, instance=epi)
        if form.is_valid():
            form.save()
            messages.success(request, "✔ EPI atualizado com sucesso!")
            return redirect('listar_epis')
        else:
            messages.error(request, "Erro ao atualizar EPI.")
    else:
        form = EPIForm(instance=epi)

    return render(request, 'epi/form.html', {
        'form': form,
        'titulo': 'Editar EPI'
    })


# ==============================
# EXCLUIR EPI
# ==============================
@login_required
def excluir_epi(request, id):
    epi = get_object_or_404(EPI, id=id)

    if request.method == 'POST':
        epi.delete()
        messages.success(request, "✔ EPI excluído com sucesso!")
        return redirect('listar_epis')

    return render(request, 'epi/excluir.html', {'epi': epi})
