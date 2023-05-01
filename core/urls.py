from django.urls import path
from .views import IndexView, ProjetosCreateView, EmpresasCreateView, PessoasCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projetos/', ProjetosCreateView.as_view(), name='projetos'),
    path('empresas/', EmpresasCreateView.as_view(), name='empresas'),
    path('pessoas/', PessoasCreateView.as_view(), name='pessoas'),
]
