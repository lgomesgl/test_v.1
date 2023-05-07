from typing import Any, Dict
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import TemplateView, CreateView, UpdateView

from django.urls import reverse_lazy

from .forms import CreateUserModelForm, ProjetoModelForm, EmpresasModelForm, PessoasModelForm
from .models import Projeto, Empresas, Pessoas
'''
    The relationship is not been save. Why?? 
    save_m2m() is not working??
'''
class IndexTemplateView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self): # contexto para a pagina html
        context = super().get_context_data()
        context['link_admin'] = '/admin'
        context['link_create_user'] = '/create_user'
        context['link_about'] = '/about'
        context['link_tabelas'] = '/tabelas'
        context['link_usuarios'] = '/usuarios'
        context['link_projetos_form'] = '/projetos'
        context['link_empresas_form'] = '/empresas'
        context['link_pessoas_form'] = '/pessoas'
        return context

class TabelasTemplateView(TemplateView):
    template_name = 'hosting.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_admin'] = '/admin'
        context['link_projetos_form'] = '/tabelas/projetos/create'
        context['link_projetos_update'] = 'tabelas/projetos/update'
        context['link_empresas_form'] = '/tabelas/empresas/create'
        context['link_emprasas_update'] = '/tabelas/empresas/update'
        context['link_pessoas_form'] = '/tabelas/pessoas/create'
        context['1ink_pessoas_update'] = '/tabelas/pessoas/update'
        context['link_home'] = ''
        return context

class AboutTemplateView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# CreateView -> Create a new instance in the table
'''
    User is the database of usuarios from django
    Columns : Usuario, Senha, Nome, Sobrenome, Email
    View to input new usuariso in database (from django.contrib.auth.models import User)
'''
class CreateUserCreateView(CreateView):
    template_name = 'create_user.html'
    model = User
    form_class = CreateUserModelForm
    success_url = reverse_lazy('create_user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Novo usuario cadastrado')
        return super(CreateUserCreateView, self).form_valid(form)

class ProjetosCreateView(LoginRequiredMixin, CreateView): 
    template_name = 'projetos.html' 
    model = Projeto
    form_class = ProjetoModelForm 
    success_url = reverse_lazy('projetos') # aonde vai ser redirecionado se o formulario tiver sucesso
    
    def get_context_data(self, **kwargs): # contexto para a pagina html
        context = super(ProjetosCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form): # se o formulario for valido
        instance = form.save(commit=False) # salvando o formulario no banco de dados
        instance.save()
        form.save_m2m()
        messages.success(self.request, 'Novo Projeto cadastrado') # mensagem de sucesso
        return super(ProjetosCreateView, self).form_valid(form)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha os dados obrigatórios!') # mensagem de erro
        return super(ProjetosCreateView, self).form_invalid(form)

    def dispatch(self, request, *args, **kwargs): # login requirement
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    
class EmpresasCreateView(LoginRequiredMixin, CreateView):
    template_name = 'empresas.html' 
    model = Empresas
    form_class = EmpresasModelForm 
    success_url = reverse_lazy('empresas') 

    def get_context_data(self, **kwargs):
        context = super(EmpresasCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form): 
        instance = form.save(commit=False) 
        instance.save()
        form.save_m2m()
        messages.success(self.request, 'Nova Empresa cadastrada') 
        return super(EmpresasCreateView, self).form_valid(form)
    
    # def post(self, request, *args,**kwargs):
    #     empresa_form = EmpresasModelForm(request.POST)
    #     if empresa_form.is_valid():
    #         instance = empresa_form.save(commit=False)
    #         instance.save()
    #         empresa_form.save_m2m()
    #     return super().post(request, *args, **kwargs)
    
    def form_invalid(self, form): 
        messages.error(self.request, 'Erro - Preencha os dados obrigatórios!') 
        return super(EmpresasCreateView, self).form_invalid(form)

    def dispatch(self, request, *args, **kwargs): 
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
        
class PessoasCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pessoas.html' 
    model = Pessoas
    form_class = PessoasModelForm 
    success_url = reverse_lazy('pessoas') 

    def get_context_data(self, **kwargs): 
        context = super(PessoasCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form): 
        form.save() 
        # inst_.save()
        # form.save_m2m()
        messages.success(self.request, 'Nova Pessoa cadastrada') 
        return super(PessoasCreateView, self).form_valid(form)
    
    def form_invalid(self, form): 
        messages.error(self.request, 'Erro - Preencha os dados obrigatórios!') 
        return super(PessoasCreateView, self).form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs): 
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
# /tabelas/update
'''
    tabelas/update -> Pesquisar a instância que queremos modificar
    tabelas/update/pk -> formulário para modificar a instância (pk=id)
''' 
class ProjetosUpTemplateView(TemplateView):
    template_name = 'domain.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = 'o projeto'
        context['link_admin'] = '/admin'
        context["all_instances"] = Projeto.objects.all()
        return context

class EmpreasasUpTemplateView(TemplateView):
    template_name = 'domain.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = 'a empresa'
        context['link_admin'] = '/admin'
        context["all_instances"] = Empresas.objects.all()
        return context 
    
class PessoasUpTemplateView(TemplateView):
    template_name = 'domain.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = 'a pessoa'
        context['link_admin'] = '/admin'
        context["all_instances"] = Pessoas.objects.all()
        return context