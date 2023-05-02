from django.urls import path
from .views import IndexTemplateView, ProjetosCreateView, EmpresasCreateView, PessoasCreateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    # path('create_user/', CreateUserCreateView.as_view(), name='create_user'),
    path('projetos/', ProjetosCreateView.as_view(), name='projetos'),
    path('empresas/', EmpresasCreateView.as_view(), name='empresas'),
    path('pessoas/', PessoasCreateView.as_view(), name='pessoas'),
]
