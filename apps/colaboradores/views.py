from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from .models import Colaborador
from apps.epi.models import EPI
from apps.emprestimos.models import Emprestimo

class HomeView(TemplateView):
    template_name = 'colaboradores/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Últimos colaboradores (já existia)
        context['ultimos_colaboradores'] = Colaborador.objects.order_by('-id')[:5]

        # Widgets do dashboard
        context["total_epis"] = EPI.objects.count()
        context["emprestados"] = Emprestimo.objects.filter(devolvido=False).count()
        context["devolvidos"] = Emprestimo.objects.filter(devolvido=True).count()

        return context


class ColaboradorList(ListView):
    model = Colaborador
    paginate_by = 20
    template_name = 'colaboradores/lista.html'

class ColaboradorCreate(CreateView):
    model = Colaborador
    fields = ['nome', 'cpf', 'setor', 'foto_colaborador']
    success_url = reverse_lazy('colaboradores:lista')
    template_name = 'colaboradores/form.html'

    def form_valid(self, form):
        messages.success(self.request, "✔ Colaborador cadastrado com sucesso!")
        return super().form_valid(form)

class ColaboradorUpdate(UpdateView):
    model = Colaborador
    fields = ['nome', 'cpf', 'setor', 'foto_colaborador']
    success_url = reverse_lazy('colaboradores:lista')
    template_name = 'colaboradores/form.html'

    def form_valid(self, form):
        messages.success(self.request, "✔ Colaborador atualizado com sucesso!")
        return super().form_valid(form)

class ColaboradorDelete(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('colaboradores:lista')
    template_name = 'colaboradores/confirma_exclusao.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "✔ Colaborador excluído com sucesso!")
        return super().delete(request, *args, **kwargs)

