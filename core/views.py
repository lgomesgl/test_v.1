from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .forms import ProjetoModelForm, EmpresasModelForm, PessoasModelForm
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
        context['link_projetos_form'] = '/projetos'
        context['link_empresas_form'] = '/empresas'
        context['link_pessoas_form'] = '/pessoas'
        return context

# CreateView -> Create a new instance in the table
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
    success_url = reverse_lazy('empresas') # aonde vai ser redirecionado se o formulario tiver sucesso

    def get_context_data(self, **kwargs): # contexto para a pagina html
        context = super(EmpresasCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form): # se o formulario for valido
        instance = form.save(commit=False) # salvando o formulario no banco de dados
        instance.save()
        form.save_m2m()
        messages.success(self.request, 'Nova Empresa cadastrada') # mensagem de sucesso
        return super(EmpresasCreateView, self).form_valid(form)
    
    # def post(self, request, *args,**kwargs):
    #     empresa_form = EmpresasModelForm(request.POST)
    #     if empresa_form.is_valid():
    #         instance = empresa_form.save(commit=False)
    #         instance.save()
    #         empresa_form.save_m2m()
    #     return super().post(request, *args, **kwargs)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha os dados obrigatórios!') # mensagem de erro
        return super(EmpresasCreateView, self).form_invalid(form)

    def dispatch(self, request, *args, **kwargs): # autenticação
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
        
class PessoasCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pessoas.html' 
    model = Pessoas
    form_class = PessoasModelForm 
    success_url = reverse_lazy('pessoas') # aonde vai ser redirecionado se o formulario tiver sucesso

    def get_context_data(self, **kwargs): # contexto para a pagina html
        context = super(PessoasCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form): # se o formulario for valido
        form.save() # salvando o formulario no banco de dados
        # inst_.save()
        # form.save_m2m()
        messages.success(self.request, 'Nova Pessoa cadastrada') # mensagem de sucesso
        return super(PessoasCreateView, self).form_valid(form)
    
    def form_invalid(self, form): # se o formulario não for válido
        messages.error(self.request, 'Erro - Preencha os dados obrigatórios!') # mensagem de erro
        return super(PessoasCreateView, self).form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs): # autenticação
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)