from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView

from django.urls import reverse_lazy

from .forms import CreateUserModelForm, ProjetoModelForm, EmpresasModelForm, PessoasModelForm
from .models import Projeto, Empresas, Pessoas
'''
    The relationship is not been save. Why?? 
    save_m2m() is not working??
'''
# Index
class IndexTemplateView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self): # contexto para a pagina html
        context = super().get_context_data()
        context['link_admin'] = '/admin'
        context['link_create_user'] = '/create_user'
        context['link_about'] = '/about'
        context['link_tabelas'] = '/tabelas'
        context['link_usuarios'] = '/users'
        context['link_projetos_form'] = '/projetos'
        context['link_empresas_form'] = '/empresas'
        context['link_pessoas_form'] = '/pessoas'
        return context

# Usuarios
'''
    user page -> a page with the details of the user
    Create a page with TemplateView, show all the instances of the table User 
    After create a page with DetailView, for datails for each instances of the table(option)
'''
class UsuariosTemplateView(TemplateView):
    template_name = 'users.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = 'home'
        context['link_admin'] = '/admin'
        context['link_tabelas'] = '/tabelas'
        context['usuarios'] = User.objects.values
        return context
        
# About
'''
    Just talk about the database and a button to show the correlations of the tables
'''
class AboutTemplateView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_admin'] = '/admin'

        context['link_tabelas'] = '/tabelas'
        return context

# Tabelas
'''
    Show all the tables
    Have links to Details/Create/Update/Delete
    
    The loop in html is not working? try use forloop.counter0
'''
class TabelasTemplateView(TemplateView):
    template_name = 'tables.html'

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
        context['tables'] = ('Projetos','Empresas','Pessoas')
        context['link_form'] = {'0':'/tabelas/projetos/create','1': '/tabelas/empresas/create','2': '/tabelas/pessoas/create'}
        return context
    
# Tables/create
'''
    Display a form to create new instances for each tables
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
    
# Tabelas/update
'''
    tabelas/update -> Seach the instance for change
    tabelas/update/pk -> Display a form to change the instance(pk = id)
''' 
class ProjetosUpTemplateView(TemplateView):
    template_name = 'tables_up.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = 'o projeto'
        context['link_admin'] = '/admin'
        context["all_instances"] = Projeto.objects.all()
        return context

class EmpreasasUpTemplateView(TemplateView):
    template_name = 'tables_up.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = 'a empresa'
        context['link_admin'] = '/admin'
        context["all_instances"] = Empresas.objects.all()
        return context 
    
class PessoasUpTemplateView(TemplateView):
    template_name = 'tables_up.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = 'a pessoa'
        context['link_admin'] = '/admin'
        context["all_instances"] = Pessoas.objects.all()
        return context