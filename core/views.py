from django.views.generic import TemplateView, FormView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Projeto, Pessoas, Empresas
from .forms import ProjetoModelForm, EmpresasModelForm, PessoasModelForm

class IndexView(TemplateView):
    template_name = 'index.html'

class ProjetosView(FormView):
    template_name = 'projetos.html' 
    form_class = ProjetoModelForm 
    success_url = reverse_lazy('projetos') # aonde vai ser redirecionado se o formulario tiver sucesso

    def get_context_data(self): # contexto para a pagina html
        context = super().get_context_data()
        return context

    def form_valid(self, form): # se o formulario for valido
        form.save() # salvando o formulario no banco de dados
        messages.success(self.request, 'Novo Projeto cadastrado') # mensagem de sucesso
        return super().form_valid(form)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha todos os dados!') # mensagem de erro
        return super().form_invalid(form)

class EmpresasView(FormView):
    template_name = 'empresas.html' 
    form_class = EmpresasModelForm 
    success_url = reverse_lazy('empresas') # aonde vai ser redirecionado se o formulario tiver sucesso

    def get_context_data(self): # contexto para a pagina html
        context = super().get_context_data()
        return context

    def form_valid(self, form): # se o formulario for valido
        form.save() # salvando o formulario no banco de dados
        messages.success(self.request, 'Nova Empresa cadastrada') # mensagem de sucesso
        return super().form_valid(form)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha todos os dados!') # mensagem de erro
        return super().form_invalid(form)

class PessoasView(FormView):
    template_name = 'pessoas.html' 
    form_class = PessoasModelForm 
    success_url = reverse_lazy('pessoas') # aonde vai ser redirecionado se o formulario tiver sucesso

    def get_context_data(self): # contexto para a pagina html
        context = super().get_context_data()
        return context

    def form_valid(self, form): # se o formulario for valido
        form.save() # salvando o formulario no banco de dados
        messages.success(self.request, 'Nova Pessoa cadastrada') # mensagem de sucesso
        return super().form_valid(form)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha todos os dados!') # mensagem de erro
        return super().form_invalid(form)
    
