from django.urls import path
from .views import IndexTemplateView, TabelasTemplateView, CreateUserCreateView, AboutTemplateView, UsuariosTemplateView, ProjetosCreateView, EmpresasCreateView, PessoasCreateView, ProjetosUpTemplateView, EmpreasasUpTemplateView, PessoasUpTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('create_user/', CreateUserCreateView.as_view(), name='create_user'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('tabelas', TabelasTemplateView.as_view(), name='tabelas'),
    path('users', UsuariosTemplateView.as_view(), name='users'),
    path('tabelas/projetos/create', ProjetosCreateView.as_view(), name='projetos'),
    path('tabelas/projetos/update', ProjetosUpTemplateView.as_view(), name='projetos_update'),
    path('tabelas/empresas/create', EmpresasCreateView.as_view(), name='empresas'),
    path('tabelas/empresas/update', EmpreasasUpTemplateView.as_view(), name='projetos_update'),
    path('tabelas/pessoas/create', PessoasCreateView.as_view(), name='pessoas'),
    path('tabelas/pessoas/update', PessoasUpTemplateView.as_view(), name='projetos_update'),
]
