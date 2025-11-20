from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from .models import Colaborador

class HomeView(TemplateView):
    template_name = 'colaboradores/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_colaboradores'] = Colaborador.objects.order_by('-id')[:5]
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

