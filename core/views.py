from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib import messages

from django.urls import reverse_lazy

from .forms import ProjetoModelForm, EmpresasModelForm, PessoasModelForm
from .models import Projeto, Empresas, Pessoas
'''
    The relationship is not been save. Why?? 
    save_m2m() is not working??
'''
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['link_admin'] = '/admin'
        context['link_projetos_form'] = '/projetos'
        context['link_empresas_form'] = '/empresas'
        context['link_pessoas_form'] = '/pessoas'
        return context

class ProjetosView(FormView):
    template_name = 'projetos.html' 
    form_class = ProjetoModelForm 
    success_url = reverse_lazy('projetos') # aonde vai ser redirecionado se o formulario tiver sucesso

    def get_context_data(self): # contexto para a pagina html
        context = super(ProjetosView, self).get_context_data()
        return context

    def form_valid(self, form): # se o formulario for valido
        inst_ = form.save(commit=False) # salvando o formulario no banco de dados
        inst_.save()
        form.save_m2m() 
        messages.success(self.request, 'Novo Projeto cadastrado') # mensagem de sucesso
        return super(ProjetosView, self).form_valid(form)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha todos os dados!') # mensagem de erro
        return super(ProjetosView, self).form_invalid(form)

class EmpresasView(FormView):
    template_name = 'empresas.html' 
    form_class = EmpresasModelForm 
    success_url = reverse_lazy('empresas') # aonde vai ser redirecionado se o formulario tiver sucesso

    def get_context_data(self): # contexto para a pagina html
        context = super(EmpresasView, self).get_context_data()
        return context

    def form_valid(self, form): # se o formulario for valido
        inst_ = form.save(commit=False) # salvando o formulario no banco de dados
        inst_.save()
        form.save_m2m()
        messages.success(self.request, 'Nova Empresa cadastrada') # mensagem de sucesso
        return super(EmpresasView, self).form_valid(form)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha todos os dados!') # mensagem de erro
        return super(EmpresasView, self).form_invalid(form)

class PessoasView(FormView):
    template_name = 'pessoas.html' 
    form_class = PessoasModelForm 
    success_url = reverse_lazy('pessoas') # aonde vai ser redirecionado se o formulario tiver sucesso

    def get_context_data(self): # contexto para a pagina html
        context = super(PessoasView, self).get_context_data()
        return context

    def form_valid(self, form): # se o formulario for valido
        inst_ = form.save(commit=False) # salvando o formulario no banco de dados
        inst_.save()
        form.save_m2m()
        messages.success(self.request, 'Nova Pessoa cadastrada') # mensagem de sucesso
        return super(PessoasView, self).form_valid(form)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha todos os dados!') # mensagem de erro
        return super(PessoasView, self).form_invalid(form)
    
